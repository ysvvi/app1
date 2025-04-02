from goods.models import Products
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline

def q_search(query):
    if not query:
        return Products.objects.none()  
    
    if query.isdigit() and len(query) <= 7:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector("name", "description")
    search_query = SearchQuery(query)  
    
    result = Products.objects.annotate(rank=SearchRank(vector, search_query)).filter(rank__gt=0).order_by("-rank")
    
   
    result = result.annotate(headLine=SearchHeadline("name", search_query, start_sel='<span style="">'))
    result = result.annotate(bodyLine=SearchHeadline("description", search_query, start_sel='<span style="">'))
    
    return result


    #keywords = [word for word in query.split() if len(word) > 2]

    #q_objects= Q()

    #for token in keywords:
        #q_objects |= Q(description__icontains=token)
        #q_objects |= Q(name_icontains=token)

    #return Products.objects.filter(q_objects)
