# Content Authoring Assistant API

## Table of Contents

1. [Overview](#overview)
2. [Setup and Running the Application](#setup-and-running-the-application)
    - [Prerequisites](#prerequisites)
    - [Running Locally](#running-locally)
    - [Running in Docker](#running-in-docker)
3. [Deployment to Google Cloud](#deployment-to-google-cloud)
4. [API Endpoints](#api-endpoints)
5. [Evaluation of Quality](#evaluation-of-quality)
6. [Optimization Strategies](#optimization-strategies)
7. [Scaling the Model](#scaling-the-model)
8. [Technical Considerations for Production](#technical-considerations-for-production)
9. [Conceptual and Technical Design](#conceptual-and-technical-design)
10. [Strategic Roadmap](#strategic-roadmap)

## Overview

The **Content Authoring Assistant API** is a scalable, cloud-native FastAPI application that generates domain-specific content based on user inputs such as keywords, domain, audience, tone, and more. The core of the application is powered by OpenAI's `gpt-3.5-turbo` model for text generation, containerized with Docker, and deployed on Google Cloud for scalability and high availability.

The API is designed to handle multiple concurrent requests with low latency and can auto-scale to meet varying traffic demands, ensuring a responsive experience for tech-savvy users who need quick, quality content.

## Setup and Running the Application

### Prerequisites

1. **Python 3.11+**
2. **Docker**
3. **Google Cloud SDK** (if deploying to Google Cloud)
4. **OpenAI API Key** (for accessing GPT models)

### Running Locally

1. **Clone the repository:**

    ```bash
    git clone https://github.com/amir0135/content-authoring-assistant.git
    cd content-authoring-assistant
    ```

2. **Set up environment variables:**

    Create a `.env` file inside the `config/` directory and add your OpenAI API key:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

3. **Install dependencies:**

    ```bash
    pip install -r config/requirements.txt
    ```

4. **Run the application:**

    ```bash
    uvicorn src.main:app --reload
    ```

5. The API will be accessible at `http://localhost:8000`.

### Running in Docker

1. **Build the Docker image:**

    ```bash
    docker build -t content-authoring-assistant -f infra/Dockerfile .
    ```

2. **Run the Docker container:**

    ```bash
    docker run -p 8000:8000 --env-file config/.env content-authoring-assistant
    ```

3. Access the API at `http://localhost:8000`.

## Deployment to Google Cloud

1. **Build and push the Docker image:**

    ```bash
    gcloud builds submit --tag gcr.io/[PROJECT-ID]/content-authoring-assistant
    ```

2. **Deploy to Google Cloud Run:**

    ```bash
    gcloud run deploy --image gcr.io/[PROJECT-ID]/content-authoring-assistant --platform managed --region europe-west1 --allow-unauthenticated
    ```

## API Endpoints

- `POST /generate-text/`: Generates text based on the input parameters such as prompt, domain, audience, tone, etc.

  Example request:

  ```json
  {
      "prompt": "Write a blog post about AI advancements.",
      "max_tokens": 100,
      "temperature": 0.7,
      "top_p": 0.9,
      "frequency_penalty": 0.0,
      "presence_penalty": 0.0,
      "domain": "technology",
      "audience": "general",
      "tone": "informative",
      "keywords": "AI, technology"
  }
  ```

## Evaluation of Quality

### Approaches

1. **Human Evaluation**: Review the generated text for coherence, relevance, and fluency.
2. **Automated Metrics**: Use metrics such as BLEU and ROUGE to measure quality.
3. **Load Testing**: Measure response time and throughput using the `test.js` script for performance testing.

### Performance Testing

The project includes `test.js` for load testing. To run:

```bash
node src/test.js
```

## Optimization Strategies

1. **Model Distillation**: Switch to smaller models like `distilgpt2` for faster inference without sacrificing much quality.
2. **Batch Requests**: Process multiple requests in a single API call to improve efficiency.
3. **Caching**: Cache frequently requested prompts to reduce API calls to the model.

## Scaling the Model

1. **Kubernetes HPA**: The Horizontal Pod Autoscaler scales up or down based on CPU utilization.
2. **Multilingual Models**: Incorporate models like `mBART` for multi-language support.
3. **Custom Fine-Tuning**: Fine-tune GPT models for specific domains or industries.

## Technical Considerations for Production

1. **Security**: Secure API access using API keys, OAuth, and HTTPS.
2. **Latency**: Optimize response times by choosing smaller models and limiting output lengths.
3. **Concurrency**: Google Cloud Run handles up to 10 concurrent requests and can autoscale to accommodate higher traffic.
4. **Data Residency**: Ensure data processing complies with GDPR, and all data is stored and processed within the EU.

## Conceptual and Technical Design

### Key Tools and Technologies:

1. **API Framework**: FastAPI for fast and efficient API development.
2. **Text Generation**: OpenAI's `gpt-3.5-turbo` model.
3. **Containerization**: Docker for containerizing the application.
4. **Cloud Deployment**: Google Cloud Run for scalable, serverless deployment.
5. **Monitoring and Scaling**: Kubernetes Horizontal Pod Autoscaler (HPA).

### Design Overview:

- **API Gateway**: Exposes public-facing endpoints.
- **Service Layer**: FastAPI for handling requests and processing user input.
- **Model Layer**: GPT-3.5 Turbo for generating domain-specific content.
- **Autoscaling Layer**: Kubernetes HPA for scaling based on traffic.

## Strategic Roadmap

1. **Short-Term**: Optimize inference times, improve model response times, and extend the API to handle more input parameters.
2. **Mid-Term**: Add support for multiple languages and fine-tune models for specific use cases.
3. **Long-Term**: Implement automated quality checks and feedback loops for continuous improvement of content generation.
