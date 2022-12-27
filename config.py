import os
import dotenv

dotenv.load_dotenv()

datasource_host = str(os.environ.get("DATASOURCE_HOST" "localhost"))
datasource_port = str(os.environ.get("DATASOURCE_PORT" "27017"))
datasource_database = str(os.environ.get("DATASOURCE_DB" "tarefas"))
datasource_username = str(os.environ.get("DATASOURCE_USERNAME" ""))
datasource_password = str(os.environ.get("DATASOURCE_PASSWORD" ""))