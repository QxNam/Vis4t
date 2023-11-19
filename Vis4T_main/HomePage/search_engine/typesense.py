from .configs import *
import typesense

def upsert_student(students, teacher_id):
    client = typesense.Client({
    'nodes': [{
        'host': TYPESENSE_HOST,
        'port': '443',
        'protocol': 'https'
    }],
        'api_key': TYPESENSE_ADMIN_KEY,
        'connection_timeout_seconds': 10
    })
    client.collections[teacher_id].documents.upsert(students)

def search_for_student(query, teacher_id, page=1,per_page=10):
    client = typesense.Client({
    'nodes': [{
        'host': TYPESENSE_HOST,
        'port': '443',
        'protocol': 'https'
    }],
        'api_key': TYPESENSE_SEARCH_KEY,
        'connection_timeout_seconds': 10
    })
    search_parameters = {
        'q': query,
        'exhaustive_search': 'true',
        'collection': teacher_id,
        'query_by': 'embedding,lastname,student_name',
        'sort_by': '_text_match:desc,_vector_distance:asc',
        'prioritize_exact_match': 'true',
        'prioritize_token_position': 'true',
        'num_typos': '1',
        'vector_query': f'embedding:([], distance_threshold:0.50)',
        'per_page': per_page,
        'page': page
    }

    def extract(result):
        result = result['document']
        result.pop('embedding', None)
        result.pop('id', None)
        return result
    
    results = client.multi_search.perform({
        'searches': [search_parameters]
    }, {})
    try:
        results = results['results'][0]['hits']
        return list(map(extract, results))
    except:
        return results