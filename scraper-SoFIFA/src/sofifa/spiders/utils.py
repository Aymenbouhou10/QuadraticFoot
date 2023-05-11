YEAR_KEYS = {
    "23": "230024",
    "22": "220069",
    "21": "210059",
    "20": "200057",
    "19": "190057",
    "18": "180055",
    "17": "170099",
    "16": "160058",
    "15": "150059",
    "14": "140052",
    "13": "130034",
    "12": "120002",
    "11": "110002",
    "10": "100002",
    "09": "090002",
    "08": "080002",
    "07": "070002",
}

SITE_BASE_URL = "https://sofifa.com"
PLAYERS_BASE_URL = "https://sofifa.com/players?set=true&col=oa&sort=desc&showCol%5B0%5D=pi&showCol%5B1%5D=ae&showCol%5B2%5D=hi&showCol%5B3%5D=wi&showCol%5B4%5D=pf&showCol%5B5%5D=oa&showCol%5B6%5D=pt&showCol%5B7%5D=bo&showCol%5B8%5D=bp&showCol%5B9%5D=gu&showCol%5B10%5D=jt&showCol%5B11%5D=le&showCol%5B12%5D=vl&showCol%5B13%5D=wg&showCol%5B14%5D=rc&showCol%5B15%5D=ta&showCol%5B16%5D=cr&showCol%5B17%5D=fi&showCol%5B18%5D=he&showCol%5B19%5D=sh&showCol%5B20%5D=vo&showCol%5B21%5D=ts&showCol%5B22%5D=dr&showCol%5B23%5D=cu&showCol%5B24%5D=fr&showCol%5B25%5D=lo&showCol%5B26%5D=bl&showCol%5B27%5D=to&showCol%5B28%5D=ac&showCol%5B29%5D=sp&showCol%5B30%5D=ag&showCol%5B31%5D=re&showCol%5B32%5D=ba&showCol%5B33%5D=tp&showCol%5B34%5D=so&showCol%5B35%5D=ju&showCol%5B36%5D=st&showCol%5B37%5D=sr&showCol%5B38%5D=ln&showCol%5B39%5D=te&showCol%5B40%5D=ar&showCol%5B41%5D=in&showCol%5B42%5D=po&showCol%5B43%5D=vi&showCol%5B44%5D=pe&showCol%5B45%5D=cm&showCol%5B46%5D=td&showCol%5B47%5D=ma&showCol%5B48%5D=sa&showCol%5B49%5D=sl&showCol%5B50%5D=tg&showCol%5B51%5D=gd&showCol%5B52%5D=gh&showCol%5B53%5D=gk&showCol%5B54%5D=gp&showCol%5B55%5D=gr&showCol%5B56%5D=tt&showCol%5B57%5D=bs&showCol%5B58%5D=wk&showCol%5B59%5D=sk&showCol%5B60%5D=aw&showCol%5B61%5D=dw&showCol%5B62%5D=ir&showCol%5B63%5D=pac&showCol%5B64%5D=sho&showCol%5B65%5D=pas&showCol%5B66%5D=dri&showCol%5B67%5D=def&showCol%5B68%5D=phy&r=230024"
COLUMNS_REMAPPING = {
    "height": "height",
    "weight": "weight_kg",
    "crossing": "attacking_crossing",
    "finishing": "attacking_finishing",
    "heading_accuracy": "attacking_heading_accuracy",
    "short_passing": "attacking_short_passing",
    "volleys": "attacking_volleys",
    "dribbling": "skill_dribbling",
    "curve": "skill_curve",
    "fk_accuracy": "skill_fk_accuracy",
    "long_passing": "skill_long_passing",
    "ball_control": "skill_ball_control",
    "acceleration": "movement_acceleration",
    "sprint_speed": "movement_sprint_speed",
    "agility": "movement_agility",
    "reactions": "movement_reactions",
    "balance": "movement_balance",
    "shot_power": "power_shot_power",
    "jumping": "power_jumping",
    "stamina": "power_stamina",
    "strength": "power_strength",
    "long_shots": "power_long_shots",
    "aggression": "mentality_aggression",
    "interceptions": "mentality_interceptions",
    "positioning": "mentality_positioning",
    "vision": "mentality_vision",
    "penalties": "mentality_penalties",
    "composure": "mentality_composure",
    "marking": "defending_marking",
    "standing_tackle": "defending_standing_tackle",
    "sliding_tackle": "defending_sliding_tackle",
    "w/f": "weak_foot",
    "a/w": "work_rate_attack",
    "d/w": "work_rate_defense",
}


def clean_string(input_str: str) -> str:
    return input_str.strip().lower().replace(" ", "_")


def rename_columns(columns: list) -> list:
    ret = []
    for col_name in columns:
        if col_name in COLUMNS_REMAPPING.keys():
            ret.append(COLUMNS_REMAPPING[col_name])
        else:
            ret.append(col_name)
    return ret
