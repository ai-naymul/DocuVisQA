# DocsVisqa 📚🔍

DocsVisqa is a multi-functional application that leverages the power of Google's Gemini Pro API to provide various services such as searching within PDFs, image recognition, and chatbot functionality. 

## Features 🛠️

1. **PDF Search** 📄: This feature allows users to upload a PDF file and ask questions related to the content of the PDF. The application will then search within the PDF and provide the most relevant answer. This can be particularly useful for quickly finding information within large documents.

2. **Image Recognition** 🖼️: This feature allows users to upload an image and ask questions about it. The application will then analyze the image and provide a response. This can be useful for understanding the content of an image without manual inspection.

3. **Chatbot** 🤖: This feature allows users to interact with a chatbot powered by the Gemini Pro API. The chatbot can answer a wide range of questions and provide useful information.

## Local Setup or Installation 🛠️

To set up this project on your local machine, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
	```git clone https://github.com/ai-naymul/DocsVisqa.git```

2. **Navigate to the Project Directory**: After cloning, navigate to the project directory:
	```cd DocsVisqa```

3. **Install Dependencies**: Install the required dependencies by running:
	```pip install -r requirements.txt```

4. **Set Environment Variables**: Create a `.env` file in the root of the project and add your Google API key:
	- GOOGLE_API_KEY=your_api_key_here

    Make sure to replace `your_api_key_here` with your actual API key. This file is included in the `.gitignore` to prevent it from being committed to the repository.

5. **Run the Streamlit App**: Start the Streamlit app using the following command:
	```streamlit run Home.py```


This will open the app in your default web browser.

Now you're all set to explore and interact with the DocsVisqa Streamlit app locally! Congratulations🎉

## Usage 🚀

To use this application, simply navigate to the desired feature (PDF Search, Image Recognition, or Chatbot) and follow the prompts. For PDF Search and Image Recognition, you will need to upload a file. For the Chatbot, simply type your question into the input field and press "Ask the question". 🖱️

## License 📄

This project is licensed under the MIT License - see the LICENSE.md file for details.

# Contribution Guide 👥

This project is open source and we welcome contributions! 🎉

## Getting Started 🚀

1. **Fork the Repository**: Click on the 'Fork' button at the top right corner of this page. This will create a copy of this repository in your account.

2. **Clone the Repository**: Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the 'Code' button and then click the 'copy to clipboard' icon to get the URL. Use the following command to clone it to your local machine.
    ```git clone https://github.com/ai-naymul/DocsVisqa.git```

3. **Create a New Branch**: Navigate to the directory where the project is located on your machine. Create a new branch using the [git checkout](file:///e%3A/My%20Project/DocuVisQA/pages/5_%F0%9F%A4%9D_Contribute.py#19%2C132-19%2C132) command:
    ```git commit -m "Your commit message"```

2. Push your changes using the [git push](file:///e%3A/My%20Project/DocuVisQA/pages/5_%F0%9F%A4%9D_Contribute.py#33%2C33-33%2C33) command:
    ```git push origin your_new_branch_name```

3. Go to your repository on GitHub, you'll see a 'Compare & pull request' button. Click on that button to submit a pull request.

That's it! You've just made your first contribution. 🎉

## Questions ❓

If you have any questions or run into any issues, please open an issue and we'll do our best to help.

Happy coding! 💻