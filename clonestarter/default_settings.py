import os
import cloudinary

DEBUG=True

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR + "/app.db"

cloudinary.config( 
  cloud_name = "dk3btogkl", 
  api_key = "756496171926584", 
  api_secret = "Q7rHpKtHks5uumDpevY6J7Rmtvk" 
)