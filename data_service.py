from fastapi import HTTPException, status
from config import supabase
from models import DataItem, DataItemResponse, DataItemUpdate
from typing import List, Optional
from datetime import datetime

class DataService:
    def __init__(self):
        self.supabase = supabase
        self.table_name = "user_data"

    async def create_item(self, item: DataItem, user_id: str) -> DataItemResponse:
        """Create a new data item for the user"""
        try:
            data = {
                "title": item.title,
                "content": item.content,
                "metadata": item.metadata,
                "user_id": user_id
            }
            
            result = self.supabase.table(self.table_name).insert(data).execute()
            
            if not result.data:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Failed to create item"
                )
            
            created_item = result.data[0]
            return DataItemResponse(
                id=created_item["id"],
                title=created_item["title"],
                content=created_item["content"],
                metadata=created_item["metadata"],
                user_id=created_item["user_id"],
                created_at=datetime.fromisoformat(created_item["created_at"].replace('Z', '+00:00')),
                updated_at=datetime.fromisoformat(created_item["updated_at"].replace('Z', '+00:00'))
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to create item: {str(e)}"
            )

    async def get_user_items(self, user_id: str, limit: int = 100, offset: int = 0) -> List[DataItemResponse]:
        """Get all items for a specific user"""
        try:
            result = self.supabase.table(self.table_name)\
                .select("*")\
                .eq("user_id", user_id)\
                .order("created_at", desc=True)\
                .limit(limit)\
                .offset(offset)\
                .execute()
            
            items = []
            for item in result.data:
                items.append(DataItemResponse(
                    id=item["id"],
                    title=item["title"],
                    content=item["content"],
                    metadata=item["metadata"],
                    user_id=item["user_id"],
                    created_at=datetime.fromisoformat(item["created_at"].replace('Z', '+00:00')),
                    updated_at=datetime.fromisoformat(item["updated_at"].replace('Z', '+00:00'))
                ))
            
            return items
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to fetch items: {str(e)}"
            )

    async def get_item_by_id(self, item_id: str, user_id: str) -> DataItemResponse:
        """Get a specific item by ID for the user"""
        try:
            result = self.supabase.table(self.table_name)\
                .select("*")\
                .eq("id", item_id)\
                .eq("user_id", user_id)\
                .execute()
            
            if not result.data:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Item not found"
                )
            
            item = result.data[0]
            return DataItemResponse(
                id=item["id"],
                title=item["title"],
                content=item["content"],
                metadata=item["metadata"],
                user_id=item["user_id"],
                created_at=datetime.fromisoformat(item["created_at"].replace('Z', '+00:00')),
                updated_at=datetime.fromisoformat(item["updated_at"].replace('Z', '+00:00'))
            )
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to fetch item: {str(e)}"
            )

    async def update_item(self, item_id: str, item_update: DataItemUpdate, user_id: str) -> DataItemResponse:
        """Update a specific item"""
        try:
            # Build update data excluding None values
            update_data = {}
            if item_update.title is not None:
                update_data["title"] = item_update.title
            if item_update.content is not None:
                update_data["content"] = item_update.content
            if item_update.metadata is not None:
                update_data["metadata"] = item_update.metadata
            
            if not update_data:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="No fields to update"
                )
            
            result = self.supabase.table(self.table_name)\
                .update(update_data)\
                .eq("id", item_id)\
                .eq("user_id", user_id)\
                .execute()
            
            if not result.data:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Item not found or not authorized"
                )
            
            updated_item = result.data[0]
            return DataItemResponse(
                id=updated_item["id"],
                title=updated_item["title"],
                content=updated_item["content"],
                metadata=updated_item["metadata"],
                user_id=updated_item["user_id"],
                created_at=datetime.fromisoformat(updated_item["created_at"].replace('Z', '+00:00')),
                updated_at=datetime.fromisoformat(updated_item["updated_at"].replace('Z', '+00:00'))
            )
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to update item: {str(e)}"
            )

    async def delete_item(self, item_id: str, user_id: str) -> dict:
        """Delete a specific item"""
        try:
            result = self.supabase.table(self.table_name)\
                .delete()\
                .eq("id", item_id)\
                .eq("user_id", user_id)\
                .execute()
            
            if not result.data:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Item not found or not authorized"
                )
            
            return {"message": "Item deleted successfully"}
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to delete item: {str(e)}"
            )

# Create data service instance
data_service = DataService()