"""Seed data for the plant database — returns lists of dicts for each table."""


def plant_base_data():
    """Returns basic plant info: name, search key, type, water level, and size."""
    data = [
    {"name": "Manjericão",       "search_name": "manjericao",  "type": "Erva",      "water_per_day": "média", "size": "pequeno"},
    {"name": "Hortelã",          "search_name": "hortela",     "type": "Erva",      "water_per_day": "alta",  "size": "pequeno"},
    {"name": "Alecrim",          "search_name": "alecrim",     "type": "Erva",      "water_per_day": "baixa", "size": "médio"},
    {"name": "Salsa",            "search_name": "salsa",       "type": "Erva",      "water_per_day": "média", "size": "pequeno"},
    {"name": "Tomate",           "search_name": "tomate",      "type": "Fruta",    "water_per_day": "alta",  "size": "grande"},
    {"name": "Alface",           "search_name": "alface",      "type": "Verdura",   "water_per_day": "média", "size": "pequeno"},
    {"name": "Pimentão",         "search_name": "pimentao",    "type": "Legume",    "water_per_day": "média", "size": "médio"},
    {"name": "Cenoura",          "search_name": "cenoura",     "type": "Legume",    "water_per_day": "média", "size": "pequeno"},
    {"name": "Lavanda",          "search_name": "lavanda",     "type": "Flor",      "water_per_day": "baixa", "size": "médio"},
    {"name": "Girassol",         "search_name": "girassol",    "type": "Flor",      "water_per_day": "média", "size": "grande"},
    {"name": "Calêndula",        "search_name": "calendula",   "type": "Flor",      "water_per_day": "baixa", "size": "pequeno"},
    {"name": "Babosa",           "search_name": "babosa",      "type": "Suculenta", "water_per_day": "baixa", "size": "médio"},
    {"name": "Planta-jade",      "search_name": "planta-jade", "type": "Suculenta", "water_per_day": "baixa", "size": "pequeno"},
    {"name": "Bananeira",        "search_name": "bananeira",   "type": "Fruta",     "water_per_day": "alta",  "size": "grande"},
    {"name": "Morangueiro",      "search_name": "morangueiro", "type": "Fruta",     "water_per_day": "alta",  "size": "pequeno"}
    ]
    return data

def plant_water_data():
    """Returns watering schedule data: frequency, winter frequency, method, and amount."""
    data = [
        {"search_name": "manjericao",  "water_every_days": 2,  "water_every_days_winter": 3,
         "water_method": "por_cima",        "water_amount": "Até a terra ficar úmida, sem encharcar"},
        {"search_name": "hortela",     "water_every_days": 2,  "water_every_days_winter": 3,
         "water_method": "por_cima",        "water_amount": "Manter a terra sempre úmida"},
        {"search_name": "alecrim",     "water_every_days": 6,  "water_every_days_winter": 10,
         "water_method": "encharcar_secar", "water_amount": "Regar bem e esperar a terra secar antes de regar de novo"},
        {"search_name": "salsa",       "water_every_days": 3,  "water_every_days_winter": 4,
         "water_method": "por_cima",        "water_amount": "Terra úmida, sem poças"},
        {"search_name": "tomate",      "water_every_days": 2,  "water_every_days_winter": 3,
         "water_method": "por_cima",        "water_amount": "Rega abundante na base, sem molhar as folhas"},
        {"search_name": "alface",      "water_every_days": 2,  "water_every_days_winter": 3,
         "water_method": "por_cima",        "water_amount": "Rega leve e frequente, terra sempre úmida"},
        {"search_name": "pimentao",    "water_every_days": 3,  "water_every_days_winter": 5,
         "water_method": "por_cima",        "water_amount": "Rega moderada na base da planta"},
        {"search_name": "cenoura",     "water_every_days": 3,  "water_every_days_winter": 5,
         "water_method": "por_cima",        "water_amount": "Rega profunda e regular para a raiz crescer reta"},
        {"search_name": "lavanda",     "water_every_days": 7,  "water_every_days_winter": 14,
         "water_method": "encharcar_secar", "water_amount": "Pouca água, a terra precisa secar entre as regas"},
        {"search_name": "girassol",    "water_every_days": 3,  "water_every_days_winter": 5,
         "water_method": "por_cima",        "water_amount": "Rega profunda na base"},
        {"search_name": "calendula",   "water_every_days": 4,  "water_every_days_winter": 7,
         "water_method": "por_cima",        "water_amount": "Rega moderada, evitar encharcar"},
        {"search_name": "babosa",      "water_every_days": 14, "water_every_days_winter": 21,
         "water_method": "encharcar_secar", "water_amount": "Regar bem e deixar a terra secar por completo"},
        {"search_name": "planta-jade", "water_every_days": 14, "water_every_days_winter": 21,
         "water_method": "encharcar_secar", "water_amount": "Regar bem e deixar a terra secar por completo"},
        {"search_name": "bananeira",   "water_every_days": 2,  "water_every_days_winter": 3,
         "water_method": "por_cima",        "water_amount": "Rega abundante, terra sempre úmida"},
        {"search_name": "morangueiro", "water_every_days": 2,  "water_every_days_winter": 3,
         "water_method": "por_baixo",       "water_amount": "Terra úmida, evitar molhar frutos e folhas"},
    ]
    return data

def plant_sun_data():
    """Returns sunlight requirements: light level, best time, direct hours, and notes."""
    data = [
        {"search_name": "manjericao",  "light_level": "sol_pleno",    "direct_sun_hours": 6,
         "best_sun_time": "dia_todo", "sun_notes": "Precisa de pelo menos 6 horas de sol direto por dia"},
        {"search_name": "hortela",     "light_level": "meia_sombra",  "direct_sun_hours": 4,
         "best_sun_time": "manha",    "sun_notes": "Sol da manhã e sombra à tarde, o calor forte queima as folhas"},
        {"search_name": "alecrim",     "light_level": "sol_pleno",    "direct_sun_hours": 8,
         "best_sun_time": "dia_todo", "sun_notes": "Gosta de sol forte e ambiente bem ventilado"},
        {"search_name": "salsa",       "light_level": "meia_sombra",  "direct_sun_hours": 4,
         "best_sun_time": "manha",    "sun_notes": "Tolera sol pleno, mas rende melhor com sol da manhã"},
        {"search_name": "tomate",      "light_level": "sol_pleno",    "direct_sun_hours": 8,
         "best_sun_time": "dia_todo", "sun_notes": "Com pouco sol, produz menos frutos"},
        {"search_name": "alface",      "light_level": "meia_sombra",  "direct_sun_hours": 4,
         "best_sun_time": "manha",    "sun_notes": "Sol forte da tarde deixa as folhas amargas e faz a planta florir cedo"},
        {"search_name": "pimentao",    "light_level": "sol_pleno",    "direct_sun_hours": 7,
         "best_sun_time": "dia_todo", "sun_notes": "Precisa de sol e calor para florescer e frutificar"},
        {"search_name": "cenoura",     "light_level": "sol_pleno",    "direct_sun_hours": 6,
         "best_sun_time": "dia_todo", "sun_notes": "Sem sol suficiente, a raiz fica fina"},
        {"search_name": "lavanda",     "light_level": "sol_pleno",    "direct_sun_hours": 8,
         "best_sun_time": "dia_todo", "sun_notes": "Quanto mais sol, mais flores e mais aroma"},
        {"search_name": "girassol",    "light_level": "sol_pleno",    "direct_sun_hours": 8,
         "best_sun_time": "dia_todo", "sun_notes": "A flor acompanha o sol, evite lugares sombreados"},
        {"search_name": "calendula",   "light_level": "sol_pleno",    "direct_sun_hours": 6,
         "best_sun_time": "dia_todo", "sun_notes": "Tolera meia-sombra, mas floresce menos"},
        {"search_name": "babosa",      "light_level": "luz_indireta", "direct_sun_hours": 4,
         "best_sun_time": "manha",    "sun_notes": "Muito sol forte deixa as folhas amareladas ou avermelhadas"},
        {"search_name": "planta-jade", "light_level": "sol_pleno",    "direct_sun_hours": 5,
         "best_sun_time": "manha",    "sun_notes": "Sol da manhã é ideal, o sol forte da tarde pode queimar as folhas"},
        {"search_name": "bananeira",   "light_level": "sol_pleno",    "direct_sun_hours": 8,
         "best_sun_time": "dia_todo", "sun_notes": "Precisa de muito sol e proteção contra ventos fortes"},
        {"search_name": "morangueiro", "light_level": "sol_pleno",    "direct_sun_hours": 6,
         "best_sun_time": "manha",    "sun_notes": "Sol da manhã é o melhor, no calor da tarde prefere sombra leve"},
    ]
    return data

def plant_recipe_data():
    """Returns recipe data: name, main ingredient, prep time, and 3 steps."""
    data = [
        {
            "search_name": "manjericao",
            "recipe_name": "Molho Pesto Fresco",
            "main_ingredient": "Folhas de manjericão",
            "prep_time_mins": 15,
            "step_1": "Lave e seque bem as folhas de manjericão.",
            "step_2": "Bata no processador com alho, castanhas e azeite.",
            "step_3": "Adicione o queijo parmesão, ajuste o sal e misture."
        },
        {
            "search_name": "hortela",
            "recipe_name": "Chá Gelado de Hortelã com Limão",
            "main_ingredient": "Ramos de hortelã",
            "prep_time_mins": 10,
            "step_1": "Ferva a água e faça uma infusão com as folhas de hortelã.",
            "step_2": "Coa a mistura e deixe esfriar completamente.",
            "step_3": "Adicione suco de limão, adoce a gosto e sirva com gelo."
        },
        {
            "search_name": "alecrim",
            "recipe_name": "Batatas Assadas com Alecrim",
            "main_ingredient": "Ramos de alecrim fresco",
            "prep_time_mins": 40,
            "step_1": "Corte as batatas em cubos ou gomos.",
            "step_2": "Tempere com azeite, sal grosso e raminhos de alecrim.",
            "step_3": "Asse em forno preaquecido a 200°C até dourarem."
        },
        {
            "search_name": "salsa",
            "recipe_name": "Molho Chimichurri Caseiro",
            "main_ingredient": "Salsa picada",
            "prep_time_mins": 15,
            "step_1": "Pique a salsa e o alho bem fininhos.",
            "step_2": "Misture com azeite, vinagre, orégano e pimenta.",
            "step_3": "Deixe descansar por 30 minutos antes de servir."
        },
        {
            "search_name": "tomate",
            "recipe_name": "Molho de Tomate Caseiro",
            "main_ingredient": "Tomates frescos",
            "prep_time_mins": 50,
            "step_1": "Refogue cebola e alho no azeite até dourarem.",
            "step_2": "Adicione os tomates picados e tempere com sal.",
            "step_3": "Cozinhe em fogo baixo até os tomates desmancharem."
        },
        {
            "search_name": "alface",
            "recipe_name": "Salada Verde com Molho de Iogurte",
            "main_ingredient": "Folhas de alface",
            "prep_time_mins": 10,
            "step_1": "Lave, seque e rasgue as folhas de alface.",
            "step_2": "Misture iogurte natural, limão, azeite e sal.",
            "step_3": "Regue as folhas com o molho no momento de servir."
        },
        {
            "search_name": "pimentao",
            "recipe_name": "Pimentão Recheado com Carne",
            "main_ingredient": "Pimentões inteiros",
            "prep_time_mins": 45,
            "step_1": "Corte a tampa dos pimentões e retire as sementes.",
            "step_2": "Preencha com carne moída temperada e refogada.",
            "step_3": "Leve ao forno por 30 minutos até o pimentão amaciar."
        },
        {
            "search_name": "cenoura",
            "recipe_name": "Bolo Integral de Cenoura",
            "main_ingredient": "Cenouras raladas",
            "prep_time_mins": 50,
            "step_1": "Bata as cenouras, ovos e óleo no liquidificador.",
            "step_2": "Misture o líquido com açúcar, farinha integral e fermento.",
            "step_3": "Despeje em uma forma untada e asse por 40 minutos."
        },
        {
            "search_name": "lavanda",
            "recipe_name": "Biscoitos Amanteigados de Lavanda",
            "main_ingredient": "Flores secas de lavanda",
            "prep_time_mins": 30,
            "step_1": "Misture manteiga, açúcar, farinha e lavanda triturada.",
            "step_2": "Modele os biscoitos em uma assadeira.",
            "step_3": "Asse a 180°C por cerca de 15 minutos até dourarem."
        },
        {
            "search_name": "girassol",
            "recipe_name": "Mix de Sementes Torradas",
            "main_ingredient": "Sementes de girassol",
            "prep_time_mins": 15,
            "step_1": "Aqueça uma frigideira em fogo médio.",
            "step_2": "Adicione as sementes, sal e seus temperos favoritos.",
            "step_3": "Mexa constantemente até ficarem crocantes e douradas."
        },
        {
            "search_name": "calendula",
            "recipe_name": "Chá Calmante de Calêndula",
            "main_ingredient": "Pétalas de calêndula",
            "prep_time_mins": 5,
            "step_1": "Coloque as pétalas secas em uma xícara.",
            "step_2": "Despeje água fervente por cima.",
            "step_3": "Abafe por 5 minutos, coe e sirva."
        },
        {
            "search_name": "babosa",
            "recipe_name": "Suco Detox com Aloe Vera",
            "main_ingredient": "Gel interno da folha",
            "prep_time_mins": 10,
            "step_1": "Retire e lave bem o gel transparente da babosa.",
            "step_2": "Adicione o gel ao liquidificador com abacaxi e água.",
            "step_3": "Bata bem, coe se desejar e sirva gelado."
        },
        {
            "search_name": "planta-jade",
            "recipe_name": "Chá de Folhas de Jade",
            "main_ingredient": "Folhas de jade",
            "prep_time_mins": 10,
            "step_1": "Lave bem 2 ou 3 folhas de jade.",
            "step_2": "Ferva as folhas em 250ml de água por 5 minutos.",
            "step_3": "Coa o líquido e consuma morno com moderação."
        },
        {
            "search_name": "bananeira",
            "recipe_name": "Bolo de Banana Integral",
            "main_ingredient": "Bananas maduras",
            "prep_time_mins": 45,
            "step_1": "Amasse as bananas maduras em uma tigela.",
            "step_2": "Misture os ovos, aveia, azeite e canela.",
            "step_3": "Adicione fermento e asse por 35 minutos a 180°C."
        },
        {
            "search_name": "morangueiro",
            "recipe_name": "Geleia Caseira de Morango",
            "main_ingredient": "Morangos frescos",
            "prep_time_mins": 30,
            "step_1": "Pique os morangos e coloque em uma panela com açúcar.",
            "step_2": "Adicione o suco de limão e leve ao fogo baixo.",
            "step_3": "Mexa até reduzir e atingir a consistência de geleia."
        },
    ]
    return data