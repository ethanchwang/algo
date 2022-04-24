import pickle;

def txtToList(path):
    file = open(path).read();
    return file.split('\n');

def save_as_pickle(data,data_as_string):
    with open(f'pickled_dictionaries/{data_as_string}.pkl', 'wb') as f:
        pickle.dump(data, f);

alpacas = ['vodka','gin','rum','tequila','triple sec','whiskey','whisky','bourbon']
recipe = txtToList('/workspaces/algo/alpaca/data/recipes.txt');

# print(recipe);

recipe_dict = [];
total_materials = {alcs: 0 for alcs in alpacas};

for item in recipe:
    if item[0].isnumeric():
        recipe_dict.append(item);

print(recipe_dict)

for item in recipe_dict:
    print(item)
    for alc_type in alpacas:
        if item.find(alc_type) != -1:
            print(f'{alc_type} is here')
            total_materials[alc_type] += float(item.split()[0]);

print(total_materials);

total_materials_in_ml = {alcs: total_materials[alcs]*29.57 for alcs in total_materials.keys()};

print(total_materials_in_ml)