def resolve_dependancies(deps_map, p, final_order):
    if deps_map is None:
        return final_order
    
    if p in final_order:
        return final_order
    
    for d in deps_map.get(p):
        final_order = resolve_dependancies(deps_map, d, final_order)
    final_order.append(p)

    return final_order

def build_project_order(projects, dependencies):
    final_order = list()
    deps_map = dict()
    for i in projects:
        deps_map[i] = list()

    for (p, d) in dependencies:
        deps_map.get(p).append(d)
    print(deps_map)
    
    for p in projects:
        if p not in final_order:
            final_order = resolve_dependancies(deps_map, p, final_order)

    return final_order


projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'b'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

print("\n")
print(build_project_order(projects, dependencies))
print("\n")
