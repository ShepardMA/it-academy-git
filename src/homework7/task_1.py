def combine_routes(routes):
    combined_route = []
    for route in routes:
        if combined_route and combined_route[-1] == route[0]:
            combined_route.extend(route[1:])
        else:
            combined_route.extend(route)
    return combined_route


