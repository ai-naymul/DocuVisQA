import streamlit as st

# Set the page config
st.set_page_config(page_title="Contribution Guide", page_icon='👥')

# Add a header
st.header("Contribution Guide")

st.markdown("""
This project is open source and we welcome contributions! 🎉

## Getting Started 🚀

1. **Fork the Repository**: Click on the 'Fork' button at the top right corner of this page. This will create a copy of this repository in your account.

2. **Clone the Repository**: Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the 'Code' button and then click the 'copy to clipboard' icon to get the URL. Use the following command to clone it to your local machine.
    ```git clone https://github.com/ai-naymul/DocuVisQA.git```

3. **Create a New Branch**: Navigate to the directory where the project is located on your machine. Create a new branch using the `git checkout` command:
    ```git checkout -b your_new_branch_name```

## Making Changes ✏️

1. Open the project in your favorite editor and make your changes.

2. Make sure to follow the code style of the project and comment your code when necessary.

## Submitting a Pull Request ✔️

1. After making your changes, commit them using the `git commit` command:
    ```git commit -m "Your commit message"```

2. Push your changes using the `git push` command:
    ```git push origin your_new_branch_name```

3. Go to your repository on GitHub, you'll see a 'Compare & pull request' button. Click on that button to submit a pull request.

That's it! You've just made your first contribution. 🎉

## Questions ❓

If you have any questions or run into any issues, please open an issue and we'll do our best to help.

Happy coding! 💻
""")
