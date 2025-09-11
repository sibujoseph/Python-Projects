from fastapi import FastAPI

app = FastAPI()

@app.get("/documents/")
async def retrieve_document(docName: string):
    return docName
