from fastapi.encoders import jsonable_encoder
from bson.regex import Regex

async def generic_query(collection_name: str, query: CommonQuery):


    skip = (query.page - 1) * query.limit
    filter_query = {}

    if query.search_value:
        # Get one sample document to inspect fields
        sample_doc = await collection.find_one()
        if sample_doc:
            regex = Regex(query.search_value, "i")
            filter_query["$or"] = [
                {key: {"$regex": regex}} 
                for key, value in sample_doc.items()
                if isinstance(value, str)
            ]

    cursor = collection.find(filter_query)\
        .sort(query.sort_by, query.dir_dir)\
        .skip(skip)\
        .limit(query.limit)

    results = await cursor.to_list(length=query.limit)
    total = await collection.count_documents(filter_query)

    return {
        "total": total,
        "page": query.page,
        "limit": query.limit,
        "items": jsonable_encoder(results)
    }
