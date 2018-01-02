
def permission(List):
    Filter = { "type": "PermissionFilter",
                    "config" : List
                 }
    return Filter
    

def geometry(shape,coordinates):
    Filter = {"type": "GeometryFilter",
                "field_name": "geometry",
                "config" : {"type": shape,
                            "coordinates": coordinates}
                }
                      
    return Filter

    
def datetime(start,end):
    Filter = {"type": "DateRangeFilter",
                "field_name" : "acquired", 
                "config":{"gte": start,
                          "lte": end}
               }
    return Filter
                   

def cloudcover(gte, lte):
    Filter= {"type": "RangeFilter",
                 "field_name": "cloud_cover",
                 "config":{"gte":gte,
                           "lte":lte
                          }
                }
    return Filter
                                       
      
def pixelres(gte, lte):
    Filter= {"type": "RangeFilter",
               "field_name": "pixel_resolution",
                "config":{"gte":gte,
                          "lte":lte
                         }
              }
    return Filter                    


def select_filters(filterlist):
    and_filter = {"type": "AndFilter",
                  "config": filterlist
                 }
    return and_filter

def endpoint_request(itemtype,and_filter):
    request = {"item_types":itemtype,
                "filter" : and_filter
              } 
    return request
    
                            
