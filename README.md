# Content Authoring Assistant

## Table of Contents
1. [Project Overview](#project-overview)
2. [Supported Functionality](#supported-functionality)
3. [Setup and Installation](#setup-and-installation)
   - [Prerequisites](#prerequisites)
   - [Installation Steps](#installation-steps)
4. [Running the Application](#running-the-application)
   - [Example Request Payload](#example-request-payload)
   - [Expected Response](#expected-response)
5. [Load Testing](#load-testing)
6. [Deployment to Kubernetes](#deployment-to-kubernetes)
7. [Evaluation and Optimization](#evaluation-and-optimization)
8. [Security and Compliance](#security-and-compliance)
9. [Strategic Roadmap](#strategic-roadmap)


## Project Overview
The **Content Authoring Assistant** is a REST API service designed to generate draft texts based on a set of user-defined parameters such as keywords, target audience, tone of voice, and domain. This service allows content creators to quickly generate drafts that can be refined iteratively, enhancing productivity and ensuring a high-quality end result.

## Supported Functionality
The Content Authoring Assistant supports the following functionality:
- **Input Parameters:**
  - `keywords`: A list of keywords or a seed sentence to guide content generation.
  - `domain`: The domain or vertical for the content (e.g., legal, advertising, e-commerce).
  - `number_of_words`: The desired length of the generated content.
  - `target_audience`: The target audience for the content (e.g., scientist vs. consumer).
  - `tone_of_voice`: The tone of voice for the content (e.g., formal, informal, playful).

- **Output:**
  - Generates fluent English text based on the provided input parameters.
  - Returns the generated text in UTF-16 format.

- **Cloud Native:** The API is cloud-native and capable of being deployed on any Kubernetes cluster.
- **Scalability:** It can handle up to 10 concurrent requests with a response time of under 10 seconds.
- **Compliance:** All data must comply with GDPR, ensuring data residency within the EU.
- **Security:** Sensitive information like API keys and database credentials should be managed using Kubernetes secrets.

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- Docker
- Kubernetes (local or cloud-based)
- K6 (for load testing)

### Installation Steps
1. **Clone the repository:**
    ```bash
    git clone https://github.com/amir0135/content-authoring-assistant.git
    cd content-authoring-assistant
    ```

2. **Install the dependencies:**
    ```bash
    pip install -r config/requirements.txt
    ```

3. **Set up environment variables:**
   Create a `.env` file in the `config/` directory with the following content:
    ```
    OPENAI_API_KEY=<your_openai_api_key>
    DATABASE_URL=<your_database_connection_string>
    ```

4. **Build the Docker image:**
    ```bash
    docker build -f infra/Dockerfile -t content-authoring-assistant .
    ```

5. **Run the Docker container:**
    ```bash
    docker run -p 8000:8000 content-authoring-assistant
    ```

## Running the Application
The API can be accessed locally or through the deployed service.

- **Local Endpoint:** `http://localhost:8000/generate-text/`
- **Deployed Endpoint:** `http://35.240.49.235/generate-text/`

### Example Request Payload
Send a POST request with the following parameters to the `/generate-text/` endpoint:

```json
{
  "keywords": "artificial intelligence, machine learning",
  "domain": "technology",
  "number_of_words": 150,
  "target_audience": "engineers",
  "tone_of_voice": "informative"
}
```

### Expected Response
The response will be a JSON object containing the generated text. An example response might look like:

```json
{
  "generated_text": "Artificial intelligence (AI) and machine learning (ML) have revolutionized the field of technology, providing innovative solutions to complex problems..."
}
```

## Load Testing
To perform load testing on the API and evaluate its performance, use the `test.js` script with K6.

1. Ensure that the application is running at `http://localhost:8000`.
2. Run the K6 load testing script:
    ```bash
    k6 run src/test.js
    ```
3. The test results will display metrics such as response time, request rate, and pass/fail checks based on the defined criteria.

## Deployment to Kubernetes

1. **Create Kubernetes secrets:**
    ```bash
    kubectl apply -f infra/secret.yaml
    ```

2. **Deploy the application:**
    ```bash
    kubectl apply -f infra/deployment.yaml
    ```

3. **Set up Horizontal Pod Autoscaling:**
    ```bash
    kubectl apply -f infra/hpa.yaml
    ```

4. **Expose the service:**
    ```bash
    kubectl apply -f infra/service.yaml
    ```

5. **Verify the deployment:**
    Check the status of your pods and services to ensure that everything is running correctly:
    ```bash
    kubectl get pods
    kubectl get svc
    ```

## Evaluation and Optimization

1. **Quality Evaluation**: The quality of the generated content can be evaluated through linguistic metrics such as fluency, coherence, and contextual accuracy.

2. **Performance Optimization**:
   - Use a more efficient transformer model configuration from the `transformers` library.
   - Implement caching and concurrency control to optimize response time.

3. **Scaling Considerations**: 
   - Use Kubernetes Horizontal Pod Autoscaler (HPA) to manage auto-scaling based on CPU or memory usage.
   - Consider optimizing the underlying model and utilizing distributed inference techniques to handle increased load.

## Security and Compliance
- **Data Security**: Sensitive information like API keys and database credentials are managed using Kubernetes secrets.
- **Compliance**: The API and its underlying infrastructure comply with GDPR, ensuring that all data storage and processing remain within the EU.

## Strategic Roadmap
1. Expand support to generate content in additional languages.
2. Integrate a more complex database retrieval mechanism to improve contextual relevance.
3. Incorporate model fine-tuning based on user feedback for iterative improvement.
4. Implement advanced evaluation metrics for automated quality scoring.

