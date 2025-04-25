
# **AI-Powered Document Builder (Dockerized)**

## **Overview**
This app allows you to generate **PDF** and **DOCX** technical documents from **Google Docs** content as a starting point. It will also pull info from the Ollama LLM to fill in gaps if needed. The app integrates with **Google Drive** and **Google Docs API** to fetch document content and uses **WeasyPrint** and **python-docx** to convert and save the content in PDF and DOCX formats.

The application is **Dockerized** for easy setup and consistent execution across different environments.

## **Features**
- Fetch content from a **single Google Doc**
- Convert the fetched content into **PDF** and **DOCX** files.
- Save the generated documents to the `data/output_docs/` directory.
- Docker-based setup for ease of installation and execution.

## **Installation (Docker)**git status
Follow these steps to set up the app using Docker:

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/tech-doc-agent.git
cd tech-doc-agent
```

### **2. Build the Docker Image**
First, **build the Docker image** from the `Dockerfile`:

```bash
docker build -t tech-doc-agent .
```

This will install all the dependencies inside the Docker container and set up the environment.

### **3. Set Up Google API Credentials**
1. Go to the **[Google Cloud Console](https://console.cloud.google.com/)** and enable the **Google Drive API** and **Google Docs API**.
2. Create **OAuth 2.0 Client Credentials** and download the `credentials.json` file.
3. Place the `credentials.json` file in the project root directory (on your local machine).
   - This file will be **copied into the Docker container** during the build process.

### **4. Run the Docker Container**
Once the image is built, you can **run the Docker container** with the following command:

```bash
docker run -p 8501:8501 -v $(pwd)/data:/app/data tech-doc-agent
```

- **`-p 8501:8501`**: Maps port 8501 inside the container to port 8501 on your local machine, which is used by Streamlit.
- **`-v $(pwd)/data:/app/data`**: Mounts the local `data` folder to the `/app/data` directory inside the container, so the generated documents can be saved locally.

### **5. Access the Application**
After running the Docker container, the app should be accessible at:

```
http://localhost:8501
```

The app allows you to interact with the **Streamlit UI** for generating documents from Google Docs.

## **Using the App**
1. **Authentication**: Upon first use, the app will prompt you to authenticate with Google and allow access to Google Drive and Docs.
2. **Input Google Doc ID**: Enter the **Google Doc ID** or provide a **Google Drive folder ID** to scrape multiple Google Docs.
3. **Select Document Type**: Choose the type of document you want to generate (e.g., **PRD**, **Technical Specification**, **User Guide**).
4. **Generate Documents**: Click the **Generate Document** button to fetch the content and generate the document in **PDF** and **DOCX** format.
5. **Download**: After the document is generated, you can download it from the `data/output_docs/` folder.

## **File Structure**
- **/data/output_docs/**: Folder where the generated documents (PDF and DOCX) are saved.
- **ui.py**: Streamlit UI for user interaction.
- **tools/**: Contains the helper functions for interacting with Google Docs and generating PDF/DOCX files.
- **Dockerfile**: Docker configuration for building the app container.
- **requirements.txt**: Python dependencies required for the app (used in Docker build).

## **Troubleshooting**
- **Authentication Errors**: Ensure you are using the correct **credentials.json** file, and that the Google APIs are enabled.
- **Missing Files**: Ensure that the `data/output_docs/` folder exists and is writable. Use `chmod +w data/output_docs/` to fix permissions if needed.
- **Permission Issues**: If you have problems with file access or permissions, ensure that the `data/output_docs/` folder exists in your local directory.

## **Future Enhancements**
- Cloud deployment for scalability (e.g., **AWS**, **Heroku**).
- Add support for other document formats like **HTML** or **Markdown**.
- Implement background processing for document generation.

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### **Key Changes:**
- The app is **Dockerized** for easy deployment.
- The **Docker setup** is the focus, reducing the need for manual setup of Python dependencies via `pip`.

---

**Phased Development Report**

---

# **AI-Powered Document Builder - Phased Development Report**

## **Phase 1: Initial Setup and Google API Integration**
### **Objective**
- Set up the environment for the project and integrate Google APIs for accessing Google Docs and Google Drive.

### **Steps Taken**
1. **Created a new project folder** and initialized a Git repository.
2. **Created OAuth 2.0 credentials** in Google Cloud Console to access Google Docs and Drive APIs.
3. Installed dependencies for Google API interaction using `google-api-python-client`, `google-auth`, `google-auth-oauthlib`, and `google-auth-httplib2`.
4. **Built authentication flow** using Google’s OAuth2 to access the user's Google Drive and Docs content.
5. Created functions to **authenticate and fetch content** from Google Docs.

### **Why**
- **OAuth 2.0 authentication** is necessary for secure access to Google Docs and Google Drive. Using Google’s APIs allows the app to interact with Google services on behalf of the user, ensuring both security and ease of access.
- This step ensures that the app can dynamically fetch content from Google Docs and integrates seamlessly into the workflow without needing to manually input document data.

### **Outcome**
- Successfully fetched content from Google Docs for further processing.

---

## **Phase 2: Document Conversion (PDF and DOCX)**
### **Objective**
- Implement functionality for converting fetched Google Docs content into **PDF** and **DOCX** formats.

### **Steps Taken**
1. **Installed WeasyPrint** and **python-docx** for document conversion.
2. Created functions to **convert Markdown** content to **PDF** using WeasyPrint.
3. Implemented a function to **convert Markdown to DOCX** using python-docx.
4. Tested the conversion using sample Google Docs content to ensure **successful document generation**.

### **Why**
- **Document conversion** is the core functionality of this app. Allowing users to generate **PDF** and **DOCX** files from Google Docs content makes the app versatile and useful for a range of professional use cases, such as generating technical documents, PRDs, or specifications.
- **WeasyPrint** was chosen because it’s a lightweight, easy-to-integrate solution for converting HTML to PDF, while **python-docx** is ideal for working with Microsoft Word documents.

### **Outcome**
- Documents are successfully converted and saved in **PDF** and **DOCX** formats.

---

## **Phase 3: Dockerization**
### **Objective**
- Dockerize the application to ensure consistent deployment across environments and simplify setup.

### **Steps Taken**
1. **Created a Dockerfile** to build the environment and install dependencies.
2. Defined instructions in the `Dockerfile` to install **Python dependencies**, system libraries for **WeasyPrint** (Cairo, Pango), and copy the project files into the container.
3. **Built and ran the Docker container**, ensuring that the app runs correctly inside the container.
4. Mounted the `data` directory for persistent storage of output files and configured Docker to map necessary ports.

### **Why**
- **Dockerization** ensures that the app works consistently across different environments (e.g., local machines, cloud, production). It eliminates the "works on my machine" problem by packaging the application with all its dependencies in a container.
- By using Docker, the app’s environment is **isolated**, making it easier to deploy, share, and maintain without worrying about operating system-specific dependencies or version mismatches.

### **Outcome**
- Successfully built the Docker image and ran the application in an isolated environment.

---

## **Phase 4: UI Integration with Streamlit**
### **Objective**
- Create a simple UI for user interaction with the app using **Streamlit**.

### **Steps Taken**
1. **Integrated Streamlit** to allow users to input Google Doc IDs or folder IDs for processing.
2. Added form inputs for selecting document type (e.g., PRD, Technical Spec).
3. Created buttons for **generating** PDF and DOCX files and providing them as download options.
4. Implemented error handling to guide the user through common issues (e.g., missing documents or authentication errors).

### **Why**
- A **user interface** was essential to make the app accessible to non-technical users. **Streamlit** was chosen because it is easy to use and fast for building interactive UIs for data-driven applications.
- The UI provides an intuitive way to interact with the app, making it easier for users to input Google Docs and generate the required documents without needing to modify the code.

### **Outcome**
- Interactive web interface allows users to easily generate and download documents.

---

## **Phase 5: Final Testing and Deployment**
### **Objective**
- Finalize testing and prepare the app for deployment.

### **Steps Taken**
1. **Tested the complete flow**, including authentication, document generation, and downloading PDFs/DOCXs.
2. Resolved any bugs or issues related to document formatting and file saving.
3. Ensured that the app runs smoothly within the Docker container and all functionalities are working as expected.
4. **Documented the process** with a detailed **README** for easy user setup and usage instructions.

### **Why**
- **Final testing** ensures the application is working as expected and free from critical bugs before it’s deployed or handed over to end-users.
- Proper documentation is key for future maintenance and user onboarding. The **README** guides users on setting up the app, running it with Docker, and troubleshooting common issues.

### **Outcome**
- The app is fully functional and ready for deployment. The documentation guides users through setup and usage.

---

## **Troubleshooting Steps**
1. **Google Authentication Issues**:
   - **Problem**: Unable to authenticate with Google APIs.
   - **Solution**: Ensure that **credentials.json** is placed in the root directory and that the **Google APIs are enabled** in the Google Cloud Console. Re-authenticate if necessary.

2. **Missing Dependencies**:
   - **Problem**: Missing required libraries (e.g., `google-api-python-client`, `WeasyPrint`, etc.).
   - **Solution**: Run `pip install -r requirements.txt` to install all dependencies. In Docker, ensure that the `requirements.txt` file is up to date and rebuild the Docker image with `docker build -t tech-doc-agent .`.

3. **Permission Issues with Output Files**:
   - **Problem**: Generated files not showing in the output directory.
   - **Solution**: Ensure the `data/output_docs/` folder exists and has proper **write permissions**. Run `chmod +w data/output_docs/` to fix permissions.

4. **Docker Container Not Starting**:
   - **Problem**: Docker container fails to start or throws errors related to missing files.
   - **Solution**: Ensure the `Dockerfile` is correctly configured and the necessary files are copied into the container. Use `docker logs <container_id>` to view error logs.

5. **Merge Conflicts with Git**:
   - **Problem**: Merge conflicts when pulling from the master branch.
   - **Solution**: Manually resolve conflicts, then commit the changes with `git add <resolved-files>` and `git commit -m "Resolved conflicts"`. Push changes with `git push origin <branch-name>`.

6. **Slow Document Generation**:
   - **Problem**: Generating large documents takes a long time.
   - **Solution**: Consider implementing background processing using tools like **Celery** for asynchronous task handling.

7. **Missing Files after Running Docker**:
   - **Problem**: Missing files or empty directories after running the Docker container.
   - **Solution**: Make sure that you're mounting the correct local directories into the Docker container using the `-v` flag during `docker run`.

8. **Google Drive/Docs Fetch Issues**:
   - **Problem**: Unable to fetch content from Google Docs.
   - **Solution**: Ensure the Google Docs ID or Drive folder ID is correct. Check that the correct API scopes are set in the OAuth configuration.

---

## **Conclusion**
This report details the **phased development** process for the AI-powered document builder application. The app is fully functional with Docker integration, Google Docs content fetching, document conversion, and a basic Streamlit UI. Troubleshooting steps are provided to assist with common issues. The app is ready for testing, deployment, and further enhancements.

---


## **Project: AI-Powered Technical Document Builder (Mac Sandbox Setup)**

---

### **Page 1: PHASE 0 \- GitHub Repo Setup**

**Step 0.1: Create Local Folder**

* **Command:** `mkdir tech-doc-agent && cd tech-doc-agent`

* **Why:** This initializes a clean project workspace for your agent project.

**Step 0.2: Set Up Virtual Environment**

* **Command:** `python3 -m venv venv && source venv/bin/activate`

* **Why:** Isolates dependencies to avoid conflicts with other Python projects on your machine.

**Step 0.3: Initialize Git Repo**

* **Command:** `git init`

* **Why:** Tracks changes and prepares project for GitHub syncing.

**Step 0.4: Add .gitignore**

* **Command:** `echo "venv/\n__pycache__/ \n*.pyc\ntoken.json\n*.pdf" >> .gitignore`

* **Why:** Prevents committing unnecessary or sensitive files.

**Step 0.5: Create GitHub Repo and Connect**

* **Action:** Created a new repo on GitHub and connected using `git remote add origin ...`

* **Why:** Enables pushing code to GitHub for version control and backup.

---

### **Page 2: PHASE 1 \- Local Dev Environment Setup**

**GitHub Step:**

* **Command:** `git add . && git commit -m "Start PHASE 1 - Local env setup" && git push`

* **Why:** Commits your folder structure and requirements setup as a checkpoint before starting coding work.

**Step 1.1: Create Folder Structure**

* **Command:** `mkdir -p tech-doc-agent/{agents,tools/templates,ui,data/input_docs,data/output_docs}`

* **Why:** Organizes the codebase into logical components for agent, tools, templates, input/output, and UI.

**Step 1.2: Activate Virtual Environment**

* **Command:** `source venv/bin/activate`

* **Why:** Ensures packages install only into this project’s environment.

**Step 1.3: Create `requirements.txt`**

**Action:** Created file in root project folder and added initial dependencies:

 streamlit  
ollama  
jinja2  
PyPDF2  
pypandoc

*   
* **Why:** Tracks all Python package requirements so setup can be replicated easily.

**Step 1.4: Install Dependencies**

* **Command:** `pip install -r requirements.txt`

* **Why:** Installs all project dependencies in one step.

**Step 1.5: Create Placeholder Files**

* **Command:** Used `touch` to create initial source files for agent logic, UI, and tools.

* **Why:** Prepares skeleton structure to start implementing features step-by-step.

**Step 1.6: Commit to GitHub**

* **Command:** `git add . && git commit -m "Set up folder structure and environment" && git push`

* **Why:** Syncs the current project state to GitHub for tracking and collaboration.

---

### **Page 3: PHASE 2 \- Install & Run LLaMA via Ollama (Mac) (Completed)**

**GitHub Step:**

* **Command:** `git add . && git commit -m "Finish PHASE 2 - Ollama install and test" && git push`

* **Why:** Captures a clean, working version of the project after confirming local model setup.

**Step 2.1: Install Ollama**

* **Action:** Downloaded and installed Ollama from [https://ollama.com/download](https://ollama.com/download)

* **Important:** You must **launch the Ollama app at least once** after installation so that the `ollama` CLI becomes available in your terminal.

* **Why:** Ollama provides a streamlined way to run large language models locally on macOS.

**Step 2.2: Pull LLaMA Model**

* **Command:** `ollama pull llama3`

* **Why:** Downloads Meta’s LLaMA 3 model to your machine for local inference.

**Step 2.3: Test the Model**

* **Command:** `ollama run llama3`

* **Why:** Confirms that the LLaMA model runs correctly and responds to prompts.

**Step 2.4: Verify Installation Works**

* **Command:** `which ollama && ollama run llama3`

* **Why:** Confirms that the `ollama` CLI is installed and callable from the terminal.

**Step 2.5: Exit Ollama Interface**

* **Action:** Pressed `Ctrl+C` to exit.

* **Why:** Ends test session and prepares for programmatic use in next phases.

---

### **Page 4: PHASE 3 \- Google Docs API Setup (Completed and Synced)**

**Handling Secrets with Environment Variables:**

Instead of committing `credentials.json` to your repository, store its path using an environment variable and load it in your code securely.

**Step A: Create a `.env` file**

In your project root, create a file named `.env` and add:

 GOOGLE\_CREDENTIALS\_PATH=credentials.json

* 

**Step B: Install `python-dotenv`**

pip install python-dotenv

**Step C: Load the variable in your `gdocs_loader.py`**

from dotenv import load\_dotenv  
import os

load\_dotenv()  
creds\_path \= os.getenv("GOOGLE\_CREDENTIALS\_PATH")

flow \= InstalledAppFlow.from\_client\_secrets\_file(creds\_path, SCOPES)

**Step D: Update `.gitignore`**

Ensure `.env`, `credentials.json`, and `token.json` are excluded:

echo ".env\\ncredentials.json\\ntoken.json" \>\> .gitignore

**Step E: Clean Git History if Needed**

If any secret files were already committed:

git rm \--cached credentials.json token.json .env

Then commit and push:

git commit \-m "Remove secrets and switch to environment variables"  
git push

**Why:** This ensures that credentials are never exposed in GitHub and allows you to easily configure different environments (dev, staging, prod) in the future.

---

### **Page 5: PHASE 4 \- Build the Document Builder Agent (Core Logic) (Completed)**

**Agent Logic:**

The core logic of the `DocumentBuilderAgent` involves generating a document by interacting with the LLaMA model through the Ollama client, using context from a Google Doc and rendering it into a structured template.

**Key Components:**

1. **Initialization (`__init__`)**: Sets up the Ollama client for LLaMA and Jinja2 for template rendering.

2. **Running the Agent (`run`)**: Receives a prompt, communicates with the model, and returns generated content.

3. **Template Rendering (`render_template`)**: Uses Jinja2 to structure the document based on the model output.

**Testing the Agent:**

In `main.py`, the agent was called with a Google Doc ID, topic, and document type. The context was fetched from the Google Doc, and the document was generated using the agent logic. The output is saved to `data/output_docs/`.

**Possible Issues & Troubleshooting:**

1. **No Output in Terminal**: If nothing is printed, ensure `print()` statements are added to check prompt and context.

2. **Empty Context**: Ensure the `get_doc_text` function returns valid context. Check for empty or malformed Google Doc content.

3. **No Model Response**: If the model is not generating content, add exception handling to catch errors during the `chat()` call.

4. **File Writing Issues**: Ensure the `data/output_docs/` folder exists. If not, create it manually (`mkdir -p data/output_docs`). Add error handling to check if files are being written properly.

---

# **PHASE 5: Document Export and Troubleshooting**

### **Exporting the Generated Document**

In this phase, we focus on exporting the generated document to various formats such as **PDF** and **DOCX**.

**Steps for Exporting Documents:**

1. **Install Export Dependencies**

Install necessary libraries:

 bash  
Copy  
`pip install pypandoc python-docx pdfkit`

*   
  * For PDF generation, ensure that `wkhtmltopdf` is installed (use `brew install wkhtmltopdf` on macOS).

2. **Create Export Functions**

   * Add functions to convert the generated Markdown into PDF and DOCX formats using `pypandoc`, `python-docx`, and `pdfkit`.

3. **Integrate Export with Document Generation**

   * After generating the document, integrate the export functionality into your `main.py` file to save the document in multiple formats (Markdown, PDF, DOCX).

### **Troubleshooting**

**Reauthentication Process (If Logged into Wrong Google Account):**

**Delete `token.json` file**: This file stores OAuth tokens for the authenticated account.

 bash  
Copy  
`rm token.json`

1.   
2. **Re-run the Script**: After deleting `token.json`, run your script again, which will trigger the OAuth flow and ask you to choose a Google account.

3. **Choose the Correct Google Account**: When prompted, select the correct Google account and grant the necessary permissions.

**Output Generation Time:**

Please note that the output files (e.g., PDF, DOCX) may take time to generate due to factors such as document length, model load time, and the export process.

**Typical Time to Generate:**

* **Simple Documents**: A few seconds to a couple of minutes.

* **Complex Documents**: A few minutes, depending on document length and export complexity.

Consider adding user feedback during the generation process (e.g., loading indicator or progress bar).

---

You can copy this content into your preferred document editor. Let me know if you need any other help\!
