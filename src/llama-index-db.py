from mistralai.client import MistralClient
from llama_index.core import SimpleDirectoryReader, Settings, VectorStoreIndex
from llama_index.embeddings.mistralai import MistralAIEmbedding
from streamlit_app import user_input, uploaded_file
from dotenv import load_dotenv
import os

class UserInputProcessor:
    def __init__(self):
        load_dotenv()
        self.mistral_api_key = os.getenv("MISTRAL_API_KEY")

    def handle_user_input(self, user_input, uploaded_file):
        content = None
        if uploaded_file is not None:
            # Check if the uploaded file is a .py file
            if uploaded_file.name.endswith('.py'):
                content = uploaded_file.read().decode("utf-8")
            else:
                return None
        else:
            content = user_input
        return content

    def process_input(self, user_input, uploaded_file):
        if user_input or uploaded_file:
            # Handle user input
            content = self.handle_user_input(user_input, uploaded_file)
            if content:  # Ensure content is not None
                # Create a directory to store the uploaded file content
                output_dir = 'uploaded_files'
                os.makedirs(output_dir, exist_ok=True)
                
                user_code_path = os.path.join(output_dir, 'input_code.txt')
                with open(user_code_path, 'w') as file:
                    file.write(content)

                reader = SimpleDirectoryReader(input_files=[user_code_path])
                documents = reader.load_data()

                # Correctly configure the Settings object
                Settings.llm = MistralAIEmbedding(model_name="codestral-latest", api_key=self.mistral_api_key)
                Settings.embed_model = MistralAIEmbedding(embed_model='mistral-embed', api_key=self.mistral_api_key)

                index = VectorStoreIndex.from_documents(documents)
                
                # Ensure the query engine is correctly configured and used
                query_engine = index.as_query_engine(similarity_top_k=2)
                response = query_engine.query(
                    "What were the two main things the author worked on before college?"
                )
                print(str(response))

# Create an instance of the class and call the method to process user input
processor = UserInputProcessor()
processor.process_input(user_input, uploaded_file)
