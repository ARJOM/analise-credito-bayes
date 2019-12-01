base = {
    "1": {
        "historico": "ruim",
        "divida": "alta",
        "garantia": "nenhuma",
        "renda": "menor15",
        "risco": "alto",
    },
    "2": {
        "historico": "desconhecido",
        "divida": "alta",
        "garantia": "nenhuma",
        "renda": "medio",
        "risco": "alto",
    },
    "3": {
        "historico": "desconhecido",
        "divida": "baixa",
        "garantia": "nenhuma",
        "renda": "medio",
        "risco": "moderado",
    },
    "4": {
        "historico": "desconhecido",
        "divida": "baixa",
        "garantia": "nenhuma",
        "renda": "maior35",
        "risco": "alto",
    },
    "5": {
        "historico": "desconhecido",
        "divida": "baixa",
        "garantia": "nenhuma",
        "renda": "maior35",
        "risco": "baixo",
    },
    "6": {
        "historico": "desconhecido",
        "divida": "baixa",
        "garantia": "adequada",
        "renda": "maior35",
        "risco": "baixo",
    },
    "7": {
        "historico": "ruim",
        "divida": "baixa",
        "garantia": "nenhuma",
        "renda": "menor15",
        "risco": "alto",
    },
    "8": {
        "historico": "ruim",
        "divida": "baixa",
        "garantia": "adequada",
        "renda": "maior35",
        "risco": "moderado",
    },
    "9": {
        "historico": "bom",
        "divida": "baixa",
        "garantia": "nenhuma",
        "renda": "maior35",
        "risco": "baixo",
    },
    "10": {
        "historico": "bom",
        "divida": "alta",
        "garantia": "adequada",
        "renda": "maior35",
        "risco": "baixo",
    }, "11": {
        "historico": "bom",
        "divida": "alta",
        "garantia": "nenhuma",
        "renda": "menor15",
        "risco": "alto",
    }, "12": {
        "historico": "bom",
        "divida": "alta",
        "garantia": "nenhuma",
        "renda": "medio",
        "risco": "moderado",
    }, "13": {
        "historico": "bom",
        "divida": "alta",
        "garantia": "nenhuma",
        "renda": "maior35",
        "risco": "baixo",
    },
    "14": {
        "historico": "ruim",
        "divida": "alta",
        "garantia": "nenhuma",
        "renda": "medio",
        "risco": "alto",
    },
}

bayes = {
    "historico": {
        "bom": {
            "alto": 0,
            "moderado": 0,
            "baixo": 0,
        },
        "desconhecido": {
            "alto": 0,
            "moderado": 0,
            "baixo": 0,
        },
        "ruim": {
            "alto": 0,
            "moderado": 0,
            "baixo": 0,
        }
    },
    "divida": {
        "alta": {
            "alto": 0,
            "moderado": 0,
            "baixo": 0,
        },
        "baixa": {
            "alto": 0,
            "moderado": 0,
            "baixo": 0,
        }
    },
    "garantia": {
        "nenhuma": {
            "alto": 0,
            "moderado": 0,
            "baixo": 0,
        },
        "adequada": {
            "alto": 0,
            "moderado": 0,
            "baixo": 0,
        }
    },
    "renda": {
        "menor15": {
            "alto": 0,
            "moderado": 0,
            "baixo": 0,
        },
        "medio": {
            "alto": 0,
            "moderado": 0,
            "baixo": 0,
        },
        "maior35": {
            "alto": 0,
            "moderado": 0,
            "baixo": 0,
        }
    },
    "risco": {
        "alto": 0,
        "moderado": 0,
        "baixo": 0
    }
}
