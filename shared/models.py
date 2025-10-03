from pydantic import BaseModel, Field
from uuid import UUID
from enum import Enum
from typing import Dict, List, Optional
from datetime import datetime

class ResourceType(str, Enum):
    email = 'email'
    commit = 'commit'
    document = 'document'
    task = 'task'

class Resource(BaseModel):
    id: UUID = Field(..., description="Unique identifier for the resource")
    type: ResourceType = Field(..., description="Type of the resource")
    source: str = Field(..., description="Source of the resource")
    content: Dict[str, str] = Field(..., description="Content of the resource")
    tags: List[str] = Field(..., description="Tags associated with the resource")
    timestamp: datetime = Field(..., description="Timestamp of the resource creation")

class Relationship(BaseModel):
    resource_id: UUID = Field(..., description="ID of the resource")
    related_resource_id: UUID = Field(..., description="ID of the related resource")
    relationship_type: str = Field(..., description="Type of relationship")