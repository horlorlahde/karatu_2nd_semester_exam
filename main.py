# Directory structure:
# .
# |- main.py (Entry point)
# |- models.py (Data models)
# |- routes/
#     |- user_routes.py (User-related routes)
#     |- book_routes.py (Book-related routes)
#     |- borrow_routes.py (Borrowing-related routes)

# main.py

from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.book_routes import router as book_router
from routes.borrow_routes import router as borrow_router

app = FastAPI()

# Register routers
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(book_router, prefix="/books", tags=["Books"])
app.include_router(borrow_router, prefix="/borrow", tags=["Borrow"])


