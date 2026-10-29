# Content Engine Prototype

**An AI-powered product image-generation pipeline built with ComfyUI, Stable Diffusion XL, Google Colab, and Gemini.**

Content Engine is a prototype designed to streamline the creation of product visuals by combining AI-assisted prompt enhancement with an image-to-image generation and upscaling workflow.

The project brings together a web application, a FastAPI backend, a database-backed job management system, and a ComfyUI image-generation workflow. The core pipeline has been assembled, but the project remains under active development, with known bugs and reliability issues that still need to be resolved.

> **Project status:** Completed prototype — functional components are assembled, but debugging, integration validation, and reliability improvements are ongoing.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [How the Pipeline Works](#how-the-pipeline-works)
- [Image Generation Workflow](#image-generation-workflow)
- [Technology Stack](#technology-stack)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Running the ComfyUI Pipeline](#running-the-comfyui-pipeline)
- [Backend API](#backend-api)
- [Configuration](#configuration)
- [Known Issues and Limitations](#known-issues-and-limitations)
- [Future Improvements](#future-improvements)

## Overview

Generating professional product imagery often requires multiple tools and manual steps, including prompt writing, model configuration, image generation, upscaling, and output management.

Content Engine explores a more structured approach to this process.

The application provides a backend foundation for accepting product information, enhancing prompts with Gemini, and creating trackable generation jobs. The ComfyUI workflow handles image processing through a graph of connected nodes, using Stable Diffusion XL to transform an input image according to a positive prompt and a negative prompt before applying AI-based upscaling.

Google Colab provides a cloud-based environment for running ComfyUI, while Google Drive is used to persist model files and workflow-related directories across sessions.

The project is a working prototype rather than a production-ready service. Although the major components and image-generation workflow have been assembled, some bugs and integration issues remain.

## Key Features

- **AI-assisted prompt enhancement:** Uses the Google Gemini API to improve product descriptions for image-generation tasks.
- **Image-to-image generation:** Uses an input image and a text prompt to guide image transformation through Stable Diffusion XL.
- **Positive and negative prompting:** Provides separate prompts to describe desired visual characteristics and discourage common image defects.
- **AI-powered upscaling:** Uses RealESRGAN x4plus to enhance the generated image.
- **Cloud-based inference environment:** Runs ComfyUI inside Google Colab.
- **Persistent model storage:** Uses Google Drive to retain model checkpoints, upscalers, inputs, outputs, and related files.
- **Remote access:** Uses ngrok to expose the ComfyUI service through a public tunnel for remote connectivity.
- **Backend job management:** Uses FastAPI and SQLAlchemy to create and retrieve image-generation job records.
- **Web application foundation:** Includes a Next.js frontend for the application interface.

## How the Pipeline Works

The intended workflow is organized into the following stages.

1. **Product information:** A product name and description are supplied through the application.
2. **Prompt enhancement:** Gemini improves the description to provide more detailed visual instructions.
3. **Job creation:** The FastAPI backend stores a generation job and returns a job identifier.
4. **Input image preparation:** An image is loaded into the ComfyUI workflow.
5. **Image generation:** Stable Diffusion XL uses the input image and prompt conditioning to generate a modified image.
6. **Image upscaling:** RealESRGAN x4plus processes the generated image to improve its resolution and visual detail.
7. **Output saving:** ComfyUI saves the resulting image to its output directory.
8. **Result management:** The application backend provides job-retrieval functionality, forming the foundation for tracking generation results.

The Gemini prompt-enhancement and backend job-management components are implemented. The ComfyUI workflow is also configured. The exact end-to-end connection between the web application's job lifecycle and the ComfyUI execution and result retrieval should be validated when running the complete system.

## Image Generation Workflow

The ComfyUI workflow is defined in `Content Engine.json` and uses the standard ComfyUI node graph.

### Workflow stages

| Stage                  | ComfyUI node             | Purpose                                                                                      |
| ---------------------- | ------------------------ | -------------------------------------------------------------------------------------------- |
| 1. Model loading       | `CheckpointLoaderSimple` | Loads the SDXL checkpoint and provides the model, CLIP, and VAE components.                  |
| 2. Input loading       | `LoadImage`              | Loads the source product image.                                                              |
| 3. Image encoding      | `VAEEncode`              | Converts the source image into a latent representation.                                      |
| 4. Prompt conditioning | `CLIPTextEncode`         | Encodes the positive and negative prompts.                                                   |
| 5. Image generation    | `KSampler`               | Generates modified latent data using the model, prompt conditioning, and denoising settings. |
| 6. Image decoding      | `VAEDecode`              | Converts the generated latent data back into an image.                                       |
| 7. Upscaler loading    | `UpscaleModelLoader`     | Loads the RealESRGAN x4plus model.                                                           |
| 8. Image upscaling     | `ImageUpscaleWithModel`  | Upscales the generated image.                                                                |
| 9. Output saving       | `SaveImage`              | Saves the final image to the ComfyUI output directory.                                       |

## Technology Stack

| Technology          | Role                                             |
| ------------------- | ------------------------------------------------ |
| Next.js             | Web application framework                        |
| React               | Frontend component library                       |
| TypeScript          | Frontend language and type safety                |
| Python              | Backend and notebook scripting                   |
| FastAPI             | Backend REST API                                 |
| Google Gemini API   | Prompt enhancement                               |
| SQLAlchemy          | Database access and ORM                          |
| ComfyUI             | Node-based image-generation workflow engine      |
| Stable Diffusion XL | Image-generation model                           |
| RealESRGAN          | AI-based image upscaling                         |
| Google Colab        | Cloud execution environment                      |
| Google Drive        | Persistent storage for models and workflow files |
| ngrok               | Remote access to the ComfyUI service             |
| Uvicorn             | ASGI server for the FastAPI backend              |

## Repository Structure

The project includes the application code and a separately maintained ComfyUI setup and workflow.

```text
content-engine-prototype/
├── backend/
│   └── app/
│       ├── api/
│       │   ├── generate.py
│       │   ├── health.py
│       │   └── jobs.py
│       ├── core/
│       │   ├── config.py
│       │   └── database.py
│       ├── models/
│       │   └── job.py
│       ├── schemas/
│       │   ├── generate.py
│       │   └── job.py
│       ├── services/
│       │   ├── generation_service.py
│       │   ├── gemini_service.py
│       │   └── job_service.py
│       └── main.py
├── frontend/
│   └── ...
├── .env.example
├── Colab_ComfyUI.ipynb
├── Content Engine.json
└── README.md
```

The notebook and workflow JSON are the two ComfyUI-related artifacts used for environment setup and image generation. If they are currently stored only on your local system, add them to the repository if you want other developers to reproduce the workflow.

### Important files

- `Colab_ComfyUI.ipynb` — Prepares the Google Colab environment, installs ComfyUI and its dependencies, configures Google Drive storage, downloads the required models, configures ngrok, and starts the ComfyUI server.
- `Content Engine.json` — Defines the ComfyUI graph for image-to-image generation, decoding, upscaling, and output saving.
- `backend/app/services/gemini_service.py` — Implements Gemini-based prompt enhancement.
- `backend/app/services/generation_service.py` — Coordinates prompt enhancement and generation-job creation.
- `backend/app/api/generate.py` — Provides the generation-job creation endpoint.
- `backend/app/api/jobs.py` — Provides job retrieval.
- `backend/app/models/job.py` — Defines the generation-job database model.
- `frontend/` — Contains the Next.js application.

## Getting Started

### Prerequisites

Install or prepare the following:

- Git
- Python and pip
- Node.js and npm
- A Google Gemini API key
- A configured database compatible with the backend's SQLAlchemy setup
- A Google account with access to Google Colab and Google Drive
- An ngrok account and authentication token
- Sufficient Colab compute resources for running SDXL and RealESRGAN

### 1. Clone the repository

```bash
git clone https://github.com/LokeshMuruganandham/content-engine-prototype.git
cd content-engine-prototype
```

### 2. Configure the backend

Create a `.env` file based on `.env.example` and configure the required credentials.

```env
GEMINI_API_KEY=your_gemini_api_key
DATABASE_URL=your_database_connection_url
COMFYUI_URL=your_comfyui_url
```

Use the actual variable names required by the checked-out configuration. If the ComfyUI service is running in Colab behind ngrok, `COMFYUI_URL` should point to the reachable tunnel URL when the backend is configured to use it.

Keep all credentials private. Do not commit API keys, database credentials, or ngrok tokens to the repository.

### 3. Install and start the backend

From the repository root:

```bash
cd backend
python -m venv .venv
```

Activate the environment.

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

Install the dependencies using the manifest available in the backend directory. If `requirements.txt` is present:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app.main:app --reload
```

The default local API address is:

```text
http://127.0.0.1:8000
```

Interactive API documentation is generally available at:

```text
http://127.0.0.1:8000/docs
```

### 4. Install and start the frontend

Open a separate terminal:

```bash
cd frontend
npm install
npm run dev
```

Open the development URL printed by Next.js, typically `http://localhost:3000`.

Ensure the frontend API configuration matches the backend's address.

## Running the ComfyUI Pipeline

The supplied notebook is designed to run the ComfyUI workflow in Google Colab.

### Step 1: Open the notebook

Open `Colab_ComfyUI.ipynb` in Google Colab and connect to a runtime with suitable GPU support.

### Step 2: Install ComfyUI

Run the initial setup cell. It updates the package environment, installs system dependencies, clones ComfyUI, and installs its Python requirements.

The notebook checks whether CUDA is available and prints the detected GPU.

### Step 3: Mount Google Drive

Authorize Google Drive access when prompted.

The notebook uses the following base directory:

```text
/content/drive/MyDrive/ComfyUI
```

It creates the required directories for model checkpoints, upscalers, inputs, outputs, temporary files, user data, and related ComfyUI resources.

### Step 4: Download and verify the models

The notebook downloads the SDXL Base checkpoint and RealESRGAN x4plus model when they are missing.

It also checks that both model files exist before proceeding.

### Step 5: Configure ngrok

Provide your ngrok authentication token in the designated notebook cell.

**Do not commit your actual token to the notebook or repository.** Use a private Colab secret or another secure method when possible.

The notebook starts an ngrok tunnel targeting port `8188` and attempts to retrieve the public URL.

### Step 6: Start ComfyUI

Run the final notebook cell to start the ComfyUI server on port `8188`.

If startup succeeds, the server should be reachable through the established tunnel. Confirm that the URL works before configuring any external client to use it.

### Step 7: Load the workflow

Open the ComfyUI interface and load `Content Engine.json`.

Verify that the required models are available and that the source image referenced by the workflow exists in the ComfyUI input directory. If necessary, upload your own product image and select it in the `LoadImage` node.

### Step 8: Generate and save an image

Review the positive prompt, negative prompt, and sampling parameters. Run the workflow and check the generated image.

The workflow decodes the output, upscales it with RealESRGAN, and saves the final image through the `SaveImage` node.

The output is written to the ComfyUI output directory, which the notebook maps to persistent Google Drive storage.

## Backend API

The backend exposes generation-job creation and retrieval endpoints.

### Create a generation job

**Method:** `POST`

**Path:** `/generate`

This endpoint accepts product details, requests prompt enhancement, and creates a generation-job record.

Illustrative request:

```json
{
  "product_name": "Minimalist Ceramic Coffee Mug",
  "product_description": "A premium ceramic mug photographed in a clean studio setting."
}
```

The response contains a job identifier and its initial status. Refer to `/docs` for the exact response schema.

### Retrieve a generation job

**Method:** `GET`

**Path:** `/jobs/{job_id}`

Retrieves a job using its identifier. The response schema includes the job status and an image URL field.

A missing job returns a `404` response.

### Health check

A health-check router is registered in the backend. Use the interactive API documentation to confirm the exact route and response format.

**Integration note:** The API's job-management capability and the ComfyUI workflow are parts of the same prototype, but the existence of these endpoints does not, by itself, guarantee that job creation automatically triggers ComfyUI execution or that generated images are automatically returned through the API.

## Configuration

| Setting                    | Purpose                                          |
| -------------------------- | ------------------------------------------------ |
| `GEMINI_API_KEY`           | Authenticates Gemini prompt-enhancement requests |
| `DATABASE_URL`             | Configures the database connection               |
| `COMFYUI_URL`              | Intended address of the ComfyUI server           |
| `NEXT_PUBLIC_API_URL`      | Intended frontend API base URL                   |
| ngrok authentication token | Authenticates the remote-access tunnel           |

The notebook currently uses Google Drive storage and a tunnel to expose the ComfyUI service. Because Colab runtimes are temporary, the public URL and runtime state may change between sessions.

## Known Issues and Limitations

The project is a completed prototype with known bugs. It should not yet be considered a production-ready service.

Areas that require attention include:

- **End-to-end integration:** Validate the complete flow from frontend input through backend job creation to ComfyUI execution and image retrieval.
- **Job lifecycle management:** Ensure job states accurately reflect queued, running, completed, and failed generations.
- **Remote connectivity:** The ngrok URL may change between sessions, and tunnel startup can fail.
- **Model availability:** Large model files may fail to download or may be missing from the expected directories.
- **Colab runtime limitations:** GPU availability, runtime disconnections, dependency conflicts, and execution limits can interrupt processing.
- **Image input configuration:** The workflow references a particular source image, which may need to be replaced with an image available in the current ComfyUI input directory.
- **Error handling:** Failures in prompt enhancement, database operations, model loading, or image generation need consistent reporting and recovery.
- **Output delivery:** Verify that generated image paths are accessible to the application and that output URLs remain valid.
- **Security:** Protect API keys and avoid exposing an unauthenticated ComfyUI instance to unintended users.

These are areas to validate and improve, not a claim that every listed failure has been observed in every run.

## Future Improvements

Potential improvements include:

- Complete and validate automated backend-to-ComfyUI workflow submission.
- Add robust job-state updates and progress reporting.
- Automatically retrieve generated images and persist their locations.
- Add retry mechanisms and more detailed error logging.
- Improve model and input validation.
- Make ngrok URL configuration easier to update between sessions.
- Add automated tests for the API, prompt-enhancement service, and workflow integration.
- Add generation history and image previews to the frontend.
- Improve deployment, access control, and operational monitoring.

---

**Content Engine Prototype** — a work in progress exploring AI-assisted product imagery through prompt enhancement, image-to-image generation, and AI-powered upscaling.
