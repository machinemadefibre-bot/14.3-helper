# -*- coding: utf-8 -*-
# Generated from armor_overmatch.json. WoWS ModsAPI blocks the json module.
DATABASE = {
  "schema": 2,
  "meta": {
    "name": "14.3-helper",
    "gameBuild": "12267945",
    "realm": "ASIA",
    "generatedAt": "2026-05-11T17:54:28",
    "source": "wowsunpack GameParams JSON, streamed per ship",
    "notes": "Armor groups are refined from armor geometry where available: deck uses broad outer horizontal deck surfaces (carriers use the highest flight deck), side uses longitudinal side surfaces from visible side or casemate armor while excluding transverse bulkheads, local superstructure/turret faces, and lower belt extensions, submarines use all positive final-hull armor values for hull armor because positional geometry is not useful there, bow/stern and extended belt conservatively remove values not visible in end plating positions, and destroyers preserve their strongest original side value because their thickest main hull plating counts as outer side armor. Armor groups are refined from armor geometry where available: deck uses broad outer horizontal deck surfaces (carriers use the highest flight deck), side uses longitudinal side surfaces from visible side or casemate armor while excluding transverse bulkheads, local superstructure/turret faces, and lower belt extensions, bow/stern and extended belt conservatively remove values not visible in end plating positions, and destroyers preserve their strongest original side value because their thickest main hull plating counts as outer side armor. Armor groups are refined from armor geometry where available: deck uses the outermost horizontal deck surface (carriers use the highest flight deck), side includes above-water side/casemate armor layers while excluding lower belt extensions, bow/stern and extended belt conservatively remove values not visible in end plating positions, carrier side uses the strongest non-belt side plating, and destroyers preserve their strongest original side value because their thickest main hull plating counts as outer side armor. Side values are refined from armor geometry and include above-water side/casemate armor layers while excluding lower belt extensions where geometry is available. Deck uses a representative weather-deck thickness rather than every deck-like material. Side means upper side plating above the main armor belt. Known armor-viewer corrections are applied for ships whose side material is not separable from client collision material groups. Armor groups are classified from collision material IDs. Deck uses a representative weather-deck thickness rather than every deck-like material. Side means upper side plating above the main armor belt. Main-gun HE/SAP penetration is resolved from projectile alphaPiercingHE/alphaPiercingCS and filtered by the largest main-gun caliber. Extraction is opt-in to avoid high memory use."
  },
  "ships": {
    "PASA002_Bogue_1942": {
      "name": "PASA002_Bogue_1942",
      "aliases": [
        "PASA002_Bogue_1942",
        "PASA002",
        "4292851696"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA004_Langley_1929": {
      "name": "PASA004_Langley_1929",
      "aliases": [
        "PASA004_Langley_1929",
        "PASA004",
        "4290754544"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA006_Independence_1945": {
      "name": "PASA006_Independence_1945",
      "aliases": [
        "PASA006_Independence_1945",
        "PASA006",
        "4288657392"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            13,
            16,
            51
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            51,
            102
          ],
          "bow": [
            51,
            102
          ],
          "stern": []
        }
      }
    },
    "PASA010_Ranger_1944": {
      "name": "PASA010_Ranger_1944",
      "aliases": [
        "PASA010_Ranger_1944",
        "PASA010",
        "4284463088"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA012_Lexington_1944": {
      "name": "PASA012_Lexington_1944",
      "aliases": [
        "PASA012_Lexington_1944",
        "PASA012",
        "4282365936"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13,
            19,
            25
          ],
          "stern": [
            13,
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA013_Essex_1945": {
      "name": "PASA013_Essex_1945",
      "aliases": [
        "PASA013_Essex_1945",
        "PASA013",
        "4281317360"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19,
            64
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA015_Midway_1945": {
      "name": "PASA015_Midway_1945",
      "aliases": [
        "PASA015_Midway_1945",
        "PASA015",
        "4279220208"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            50
          ],
          "stern": [
            19,
            50
          ]
        },
        "deck": {
          "values": [
            87
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA020_Essex": {
      "name": "PASA020_Essex",
      "aliases": [
        "PASA020_Essex",
        "PASA020",
        "4273977328"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19,
            64
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA026_Independence": {
      "name": "PASA026_Independence",
      "aliases": [
        "PASA026_Independence",
        "PASA026",
        "4267685872"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19,
            51
          ]
        },
        "deck": {
          "values": [
            21
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA028_Yorktown": {
      "name": "PASA028_Yorktown",
      "aliases": [
        "PASA028_Yorktown",
        "PASA028",
        "4265588720"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            16,
            19,
            28
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA104_Langley": {
      "name": "PASA104_Langley",
      "aliases": [
        "PASA104_Langley",
        "PASA104",
        "4185896944"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA106_Ranger": {
      "name": "PASA106_Ranger",
      "aliases": [
        "PASA106_Ranger",
        "PASA106",
        "4183799792"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA108_Lexington": {
      "name": "PASA108_Lexington",
      "aliases": [
        "PASA108_Lexington",
        "PASA108",
        "4181702640"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13,
            19,
            25
          ],
          "stern": [
            13,
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA110_Midway": {
      "name": "PASA110_Midway",
      "aliases": [
        "PASA110_Midway",
        "PASA110",
        "4179605488"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            50
          ],
          "stern": [
            19,
            50
          ]
        },
        "deck": {
          "values": [
            87
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA111_United_States": {
      "name": "PASA111_United_States",
      "aliases": [
        "PASA111_United_States",
        "PASA111",
        "4178556912"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA507_Saipan_1946": {
      "name": "PASA507_Saipan_1946",
      "aliases": [
        "PASA507_Saipan_1946",
        "PASA507",
        "3763320816"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA508_Enterprise": {
      "name": "PASA508_Enterprise",
      "aliases": [
        "PASA508_Enterprise",
        "PASA508",
        "3762272240"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            21
          ],
          "stern": [
            21,
            28
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA510_Roosevelt": {
      "name": "PASA510_Roosevelt",
      "aliases": [
        "PASA510_Roosevelt",
        "PASA510",
        "3760175088"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            50
          ],
          "stern": [
            19,
            50
          ]
        },
        "deck": {
          "values": [
            87
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA518_Enterprise": {
      "name": "PASA518_Enterprise",
      "aliases": [
        "PASA518_Enterprise",
        "PASA518",
        "3751786480"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            21
          ],
          "stern": [
            21,
            28
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA528_Saipan": {
      "name": "PASA528_Saipan",
      "aliases": [
        "PASA528_Saipan",
        "PASA528",
        "3741300720"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA538_Hornet": {
      "name": "PASA538_Hornet",
      "aliases": [
        "PASA538_Hornet",
        "PASA538",
        "3730814960"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19,
            28
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA598_Black_Saipan": {
      "name": "PASA598_Black_Saipan",
      "aliases": [
        "PASA598_Black_Saipan",
        "PASA598",
        "3667900400"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA898_AZUR_Hornet": {
      "name": "PASA898_AZUR_Hornet",
      "aliases": [
        "PASA898_AZUR_Hornet",
        "PASA898",
        "3353327600"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19,
            28
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA908_Concord_Bridge": {
      "name": "PASA908_Concord_Bridge",
      "aliases": [
        "PASA908_Concord_Bridge",
        "PASA908",
        "3342841840"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13,
            19,
            25
          ],
          "stern": [
            13,
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA910_Essex": {
      "name": "PASA910_Essex",
      "aliases": [
        "PASA910_Essex",
        "PASA910",
        "3340744688"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19,
            64
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA915_TST_Midway": {
      "name": "PASA915_TST_Midway",
      "aliases": [
        "PASA915_TST_Midway",
        "PASA915",
        "3335501808"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            50
          ],
          "stern": [
            19,
            50
          ]
        },
        "deck": {
          "values": [
            87
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASA920_Pinata_Essex": {
      "name": "PASA920_Pinata_Essex",
      "aliases": [
        "PASA920_Pinata_Essex",
        "PASA920",
        "3330258928"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19,
            64
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB001_Michigan_1916": {
      "name": "PASB001_Michigan_1916",
      "aliases": [
        "PASB001_Michigan_1916",
        "PASB001",
        "4293867504"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            254
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB004_Arkansas_1912": {
      "name": "PASB004_Arkansas_1912",
      "aliases": [
        "PASB004_Arkansas_1912",
        "PASB004",
        "4290721776"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            229
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB006_New_York_1934": {
      "name": "PASB006_New_York_1934",
      "aliases": [
        "PASB006_New_York_1934",
        "PASB006",
        "4288624624"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            280
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB008_Colorado_1945": {
      "name": "PASB008_Colorado_1945",
      "aliases": [
        "PASB008_Colorado_1945",
        "PASB008",
        "4286527472"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB012_North_Carolina_1945": {
      "name": "PASB012_North_Carolina_1945",
      "aliases": [
        "PASB012_North_Carolina_1945",
        "PASB012",
        "4282333168"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB013_Arkansas_1912": {
      "name": "PASB013_Arkansas_1912",
      "aliases": [
        "PASB013_Arkansas_1912",
        "PASB013",
        "4281284592"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            229
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB017_Montana_1945": {
      "name": "PASB017_Montana_1945",
      "aliases": [
        "PASB017_Montana_1945",
        "PASB017",
        "4277090288"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB018_Iowa_1944": {
      "name": "PASB018_Iowa_1944",
      "aliases": [
        "PASB018_Iowa_1944",
        "PASB018",
        "4276041712"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB034_New_Mexico_1941": {
      "name": "PASB034_New_Mexico_1941",
      "aliases": [
        "PASB034_New_Mexico_1941",
        "PASB034",
        "4259264496"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB108_Kansas": {
      "name": "PASB108_Kansas",
      "aliases": [
        "PASB108_Kansas",
        "PASB108",
        "4181669872"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB109_Minnesota": {
      "name": "PASB109_Minnesota",
      "aliases": [
        "PASB109_Minnesota",
        "PASB109",
        "4180621296"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB110_Vermont": {
      "name": "PASB110_Vermont",
      "aliases": [
        "PASB110_Vermont",
        "PASB110",
        "4179572720"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            51
          ]
        },
        "side": {
          "values": [
            406
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB111_Maine": {
      "name": "PASB111_Maine",
      "aliases": [
        "PASB111_Maine",
        "PASB111",
        "4178524144"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            38
          ],
          "stern": [
            32,
            38
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB208_Nebraska": {
      "name": "PASB208_Nebraska",
      "aliases": [
        "PASB208_Nebraska",
        "PASB208",
        "4076812272"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            19,
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB209_Delaware": {
      "name": "PASB209_Delaware",
      "aliases": [
        "PASB209_Delaware",
        "PASB209",
        "4075763696"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32,
            38
          ]
        },
        "deck": {
          "values": [
            19,
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB210_Louisiana": {
      "name": "PASB210_Louisiana",
      "aliases": [
        "PASB210_Louisiana",
        "PASB210",
        "4074715120"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            19,
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB505_Oklahoma": {
      "name": "PASB505_Oklahoma",
      "aliases": [
        "PASB505_Oklahoma",
        "PASB505",
        "3765385200"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB506_Arizona_1941": {
      "name": "PASB506_Arizona_1941",
      "aliases": [
        "PASB506_Arizona_1941",
        "PASB506",
        "3764336624"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26,
            37
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB507_West_Virginia": {
      "name": "PASB507_West_Virginia",
      "aliases": [
        "PASB507_West_Virginia",
        "PASB507",
        "3763288048"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB508_Alabama": {
      "name": "PASB508_Alabama",
      "aliases": [
        "PASB508_Alabama",
        "PASB508",
        "3762239472"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB509_Missouri": {
      "name": "PASB509_Missouri",
      "aliases": [
        "PASB509_Missouri",
        "PASB509",
        "3761190896"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB510_Ohio": {
      "name": "PASB510_Ohio",
      "aliases": [
        "PASB510_Ohio",
        "PASB510",
        "3760142320"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB517_Florida": {
      "name": "PASB517_Florida",
      "aliases": [
        "PASB517_Florida",
        "PASB517",
        "3752802288"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            37
          ]
        },
        "side": {
          "values": [
            26
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB518_Massachusetts": {
      "name": "PASB518_Massachusetts",
      "aliases": [
        "PASB518_Massachusetts",
        "PASB518",
        "3751753712"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB519_Kearsarge": {
      "name": "PASB519_Kearsarge",
      "aliases": [
        "PASB519_Kearsarge",
        "PASB519",
        "3750705136"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            19,
            38
          ]
        },
        "side": {
          "values": [
            38,
            330
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB527_West_Virginia_1944": {
      "name": "PASB527_West_Virginia_1944",
      "aliases": [
        "PASB527_West_Virginia_1944",
        "PASB527",
        "3742316528"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB528_Alabama_VL": {
      "name": "PASB528_Alabama_VL",
      "aliases": [
        "PASB528_Alabama_VL",
        "PASB528",
        "3741267952"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB538_Constellation": {
      "name": "PASB538_Constellation",
      "aliases": [
        "PASB538_Constellation",
        "PASB538",
        "3730782192"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            57
          ]
        },
        "side": {
          "values": [
            57
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB539_Illinois": {
      "name": "PASB539_Illinois",
      "aliases": [
        "PASB539_Illinois",
        "PASB539",
        "3729733616"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB598_Black_Massachusetts": {
      "name": "PASB598_Black_Massachusetts",
      "aliases": [
        "PASB598_Black_Massachusetts",
        "PASB598",
        "3667867632"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB599_Black_Kearsarge": {
      "name": "PASB599_Black_Kearsarge",
      "aliases": [
        "PASB599_Black_Kearsarge",
        "PASB599",
        "3666819056"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            19,
            38
          ]
        },
        "side": {
          "values": [
            38,
            330
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB705_Texas_1944": {
      "name": "PASB705_Texas_1944",
      "aliases": [
        "PASB705_Texas_1944",
        "PASB705",
        "3555670000"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            280
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB707_California": {
      "name": "PASB707_California",
      "aliases": [
        "PASB707_California",
        "PASB707",
        "3553572848"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB708_Alabama": {
      "name": "PASB708_Alabama",
      "aliases": [
        "PASB708_Alabama",
        "PASB708",
        "3552524272"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB710_Oregon": {
      "name": "PASB710_Oregon",
      "aliases": [
        "PASB710_Oregon",
        "PASB710",
        "3550427120"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB718_Tennessee": {
      "name": "PASB718_Tennessee",
      "aliases": [
        "PASB718_Tennessee",
        "PASB718",
        "3542038512"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB719_Indiana": {
      "name": "PASB719_Indiana",
      "aliases": [
        "PASB719_Indiana",
        "PASB719",
        "3540989936"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB720_Rhode_Island": {
      "name": "PASB720_Rhode_Island",
      "aliases": [
        "PASB720_Rhode_Island",
        "PASB720",
        "3539941360"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB729_Georgia": {
      "name": "PASB729_Georgia",
      "aliases": [
        "PASB729_Georgia",
        "PASB729",
        "3530504176"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB730_Wisconsin": {
      "name": "PASB730_Wisconsin",
      "aliases": [
        "PASB730_Wisconsin",
        "PASB730",
        "3529455600"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB808_Colorful_North_Carolina": {
      "name": "PASB808_Colorful_North_Carolina",
      "aliases": [
        "PASB808_Colorful_North_Carolina",
        "PASB808",
        "3447666672"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB810_TST_MONTANA": {
      "name": "PASB810_TST_MONTANA",
      "aliases": [
        "PASB810_TST_MONTANA",
        "PASB810",
        "3445569520"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB818_Black_Alabama": {
      "name": "PASB818_Black_Alabama",
      "aliases": [
        "PASB818_Black_Alabama",
        "PASB818",
        "3437180912"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB820_BA_Montana": {
      "name": "PASB820_BA_Montana",
      "aliases": [
        "PASB820_BA_Montana",
        "PASB820",
        "3435083760"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB889_Azur_Kearsarge": {
      "name": "PASB889_Azur_Kearsarge",
      "aliases": [
        "PASB889_Azur_Kearsarge",
        "PASB889",
        "3362732016"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            19,
            38
          ]
        },
        "side": {
          "values": [
            38,
            330
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB891_Maine_PLUS": {
      "name": "PASB891_Maine_PLUS",
      "aliases": [
        "PASB891_Maine_PLUS",
        "PASB891",
        "3360634864"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            38
          ],
          "stern": [
            32,
            38
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB899_Volunteer_State": {
      "name": "PASB899_Volunteer_State",
      "aliases": [
        "PASB899_Volunteer_State",
        "PASB899",
        "3352246256"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB908_East_North_Carolina_1945": {
      "name": "PASB908_East_North_Carolina_1945",
      "aliases": [
        "PASB908_East_North_Carolina_1945",
        "PASB908",
        "3342809072"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB909_Pirate_Delaware": {
      "name": "PASB909_Pirate_Delaware",
      "aliases": [
        "PASB909_Pirate_Delaware",
        "PASB909",
        "3341760496"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32,
            38
          ]
        },
        "deck": {
          "values": [
            19,
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB910_Connecticut": {
      "name": "PASB910_Connecticut",
      "aliases": [
        "PASB910_Connecticut",
        "PASB910",
        "3340711920"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            51
          ]
        },
        "side": {
          "values": [
            406
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB917_Montana_1945": {
      "name": "PASB917_Montana_1945",
      "aliases": [
        "PASB917_Montana_1945",
        "PASB917",
        "3333371888"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB918_Azur_Massachusetts": {
      "name": "PASB918_Azur_Massachusetts",
      "aliases": [
        "PASB918_Azur_Massachusetts",
        "PASB918",
        "3332323312"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB919_Iowa_2": {
      "name": "PASB919_Iowa_2",
      "aliases": [
        "PASB919_Iowa_2",
        "PASB919",
        "3331274736"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB920_Montana_2": {
      "name": "PASB920_Montana_2",
      "aliases": [
        "PASB920_Montana_2",
        "PASB920",
        "3330226160"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB930_Black_Rhode_Island": {
      "name": "PASB930_Black_Rhode_Island",
      "aliases": [
        "PASB930_Black_Rhode_Island",
        "PASB930",
        "3319740400"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB990_Utah": {
      "name": "PASB990_Utah",
      "aliases": [
        "PASB990_Utah",
        "PASB990",
        "3256825840"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            51
          ]
        },
        "side": {
          "values": [
            406
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB997_Colorado_2": {
      "name": "PASB997_Colorado_2",
      "aliases": [
        "PASB997_Colorado_2",
        "PASB997",
        "3249485808"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASB998_North_Carolina_2": {
      "name": "PASB998_North_Carolina_2",
      "aliases": [
        "PASB998_North_Carolina_2",
        "PASB998",
        "3248437232"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC001_Erie_1936": {
      "name": "PASC001_Erie_1936",
      "aliases": [
        "PASC001_Erie_1936",
        "PASC001",
        "4293834736"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC002_Chester_1908": {
      "name": "PASC002_Chester_1908",
      "aliases": [
        "PASC002_Chester_1908",
        "PASC002",
        "4292786160"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            22
          ]
        },
        "side": {
          "values": [
            22,
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC003_Albany_1898": {
      "name": "PASC003_Albany_1898",
      "aliases": [
        "PASC003_Albany_1898",
        "PASC003",
        "4291737584"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC004_St_Louis_1906": {
      "name": "PASC004_St_Louis_1906",
      "aliases": [
        "PASC004_St_Louis_1906",
        "PASC004",
        "4290689008"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13,
            102
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC005_Omaha_1923": {
      "name": "PASC005_Omaha_1923",
      "aliases": [
        "PASC005_Omaha_1923",
        "PASC005",
        "4289640432"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13,
            25
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC006_Atlanta_1942": {
      "name": "PASC006_Atlanta_1942",
      "aliases": [
        "PASC006_Atlanta_1942",
        "PASC006",
        "4288591856"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC007_Cleveland_1945": {
      "name": "PASC007_Cleveland_1945",
      "aliases": [
        "PASC007_Cleveland_1945",
        "PASC007",
        "4287543280"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16,
            51
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC011_Jacksonville": {
      "name": "PASC011_Jacksonville",
      "aliases": [
        "PASC011_Jacksonville",
        "PASC011",
        "4283348976"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC012_Pensacola_1944": {
      "name": "PASC012_Pensacola_1944",
      "aliases": [
        "PASC012_Pensacola_1944",
        "PASC012",
        "4282300400"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC014_New_Orlean_1944": {
      "name": "PASC014_New_Orlean_1944",
      "aliases": [
        "PASC014_New_Orlean_1944",
        "PASC014",
        "4280203248"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC016_Worcester_1948": {
      "name": "PASC016_Worcester_1948",
      "aliases": [
        "PASC016_Worcester_1948",
        "PASC016",
        "4278106096"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC017_Baltimore_1944": {
      "name": "PASC017_Baltimore_1944",
      "aliases": [
        "PASC017_Baltimore_1944",
        "PASC017",
        "4277057520"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC019_Burlington_1944": {
      "name": "PASC019_Burlington_1944",
      "aliases": [
        "PASC019_Burlington_1944",
        "PASC019",
        "4274960368"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC020_Des_Moines_1948": {
      "name": "PASC020_Des_Moines_1948",
      "aliases": [
        "PASC020_Des_Moines_1948",
        "PASC020",
        "4273911792"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC024_Phoenix_1917": {
      "name": "PASC024_Phoenix_1917",
      "aliases": [
        "PASC024_Phoenix_1917",
        "PASC024",
        "4269717488"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC044_Marblehead_1924": {
      "name": "PASC044_Marblehead_1924",
      "aliases": [
        "PASC044_Marblehead_1924",
        "PASC044",
        "4248745968"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC045_Marblehead_1924_Asus": {
      "name": "PASC045_Marblehead_1924_Asus",
      "aliases": [
        "PASC045_Marblehead_1924_Asus",
        "PASC045",
        "4247697392"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC106_Pensacola_1944": {
      "name": "PASC106_Pensacola_1944",
      "aliases": [
        "PASC106_Pensacola_1944",
        "PASC106",
        "4183734256"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC107_New_Orlean_1944": {
      "name": "PASC107_New_Orlean_1944",
      "aliases": [
        "PASC107_New_Orlean_1944",
        "PASC107",
        "4182685680"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC108_Baltimore_1944": {
      "name": "PASC108_Baltimore_1944",
      "aliases": [
        "PASC108_Baltimore_1944",
        "PASC108",
        "4181637104"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC109_Buffalo": {
      "name": "PASC109_Buffalo",
      "aliases": [
        "PASC109_Buffalo",
        "PASC109",
        "4180588528"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC111_Annapolis": {
      "name": "PASC111_Annapolis",
      "aliases": [
        "PASC111_Annapolis",
        "PASC111",
        "4178491376"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC206_Dallas": {
      "name": "PASC206_Dallas",
      "aliases": [
        "PASC206_Dallas",
        "PASC206",
        "4078876656"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC207_Helena": {
      "name": "PASC207_Helena",
      "aliases": [
        "PASC207_Helena",
        "PASC207",
        "4077828080"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC208_Cleveland": {
      "name": "PASC208_Cleveland",
      "aliases": [
        "PASC208_Cleveland",
        "PASC208",
        "4076779504"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC209_Seattle": {
      "name": "PASC209_Seattle",
      "aliases": [
        "PASC209_Seattle",
        "PASC209",
        "4075730928"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC210_Worcester": {
      "name": "PASC210_Worcester",
      "aliases": [
        "PASC210_Worcester",
        "PASC210",
        "4074682352"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC503_Charleston": {
      "name": "PASC503_Charleston",
      "aliases": [
        "PASC503_Charleston",
        "PASC503",
        "3767449584"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13,
            102
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC505_Rattlehead": {
      "name": "PASC505_Rattlehead",
      "aliases": [
        "PASC505_Rattlehead",
        "PASC505",
        "3765352432"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC507_Indianapolis_1945": {
      "name": "PASC507_Indianapolis_1945",
      "aliases": [
        "PASC507_Indianapolis_1945",
        "PASC507",
        "3763255280"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC508_Wichita": {
      "name": "PASC508_Wichita",
      "aliases": [
        "PASC508_Wichita",
        "PASC508",
        "3762206704"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC509_Vallejo": {
      "name": "PASC509_Vallejo",
      "aliases": [
        "PASC509_Vallejo",
        "PASC509",
        "3761158128"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC510_Alaska": {
      "name": "PASC510_Alaska",
      "aliases": [
        "PASC510_Alaska",
        "PASC510",
        "3760109552"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            36
          ]
        },
        "side": {
          "values": [
            28
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC518_Anchorage": {
      "name": "PASC518_Anchorage",
      "aliases": [
        "PASC518_Anchorage",
        "PASC518",
        "3751720944"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC519_Tulsa": {
      "name": "PASC519_Tulsa",
      "aliases": [
        "PASC519_Tulsa",
        "PASC519",
        "3750672368"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC528_Congress": {
      "name": "PASC528_Congress",
      "aliases": [
        "PASC528_Congress",
        "PASC528",
        "3741235184"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            36
          ]
        },
        "side": {
          "values": [
            28
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC538_Rochester": {
      "name": "PASC538_Rochester",
      "aliases": [
        "PASC538_Rochester",
        "PASC538",
        "3730749424"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC548_San_Diego": {
      "name": "PASC548_San_Diego",
      "aliases": [
        "PASC548_San_Diego",
        "PASC548",
        "3720263664"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 36,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC587_Black_Atlanta": {
      "name": "PASC587_Black_Atlanta",
      "aliases": [
        "PASC587_Black_Atlanta",
        "PASC587",
        "3679369200"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC597_Nueve_de_Julio_1951": {
      "name": "PASC597_Nueve_de_Julio_1951",
      "aliases": [
        "PASC597_Nueve_de_Julio_1951",
        "PASC597",
        "3668883440"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC599_Black_Alaska": {
      "name": "PASC599_Black_Alaska",
      "aliases": [
        "PASC599_Black_Alaska",
        "PASC599",
        "3666786288"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            36
          ]
        },
        "side": {
          "values": [
            28
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC610_Puerto_Rico": {
      "name": "PASC610_Puerto_Rico",
      "aliases": [
        "PASC610_Puerto_Rico",
        "PASC610",
        "3655251952"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC707_Flint": {
      "name": "PASC707_Flint",
      "aliases": [
        "PASC707_Flint",
        "PASC707",
        "3553540080"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC708_Bridgeport": {
      "name": "PASC708_Bridgeport",
      "aliases": [
        "PASC708_Bridgeport",
        "PASC708",
        "3552491504"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC710_Salem": {
      "name": "PASC710_Salem",
      "aliases": [
        "PASC710_Salem",
        "PASC710",
        "3550394352"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC718_AZUR_Montpelier": {
      "name": "PASC718_AZUR_Montpelier",
      "aliases": [
        "PASC718_AZUR_Montpelier",
        "PASC718",
        "3542005744"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC719_Cambridge": {
      "name": "PASC719_Cambridge",
      "aliases": [
        "PASC719_Cambridge",
        "PASC719",
        "3540957168"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC720_Hawaii": {
      "name": "PASC720_Hawaii",
      "aliases": [
        "PASC720_Hawaii",
        "PASC720",
        "3539908592"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            36
          ]
        },
        "side": {
          "values": [
            28
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC728_Protector": {
      "name": "PASC728_Protector",
      "aliases": [
        "PASC728_Protector",
        "PASC728",
        "3531519984"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            36
          ]
        },
        "side": {
          "values": [
            28
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC729_Fort_Worth": {
      "name": "PASC729_Fort_Worth",
      "aliases": [
        "PASC729_Fort_Worth",
        "PASC729",
        "3530471408"
      ],
      "mainGunCaliberMm": 254,
      "mainGunHePenMm": 42,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            28,
            191
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC810_Austin": {
      "name": "PASC810_Austin",
      "aliases": [
        "PASC810_Austin",
        "PASC810",
        "3445536752"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": 36,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC891_Jacksonville_PLUS": {
      "name": "PASC891_Jacksonville_PLUS",
      "aliases": [
        "PASC891_Jacksonville_PLUS",
        "PASC891",
        "3360602096"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC910_Black_Puerto_Rico": {
      "name": "PASC910_Black_Puerto_Rico",
      "aliases": [
        "PASC910_Black_Puerto_Rico",
        "PASC910",
        "3340679152"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC920_Gold_Hawaii": {
      "name": "PASC920_Gold_Hawaii",
      "aliases": [
        "PASC920_Gold_Hawaii",
        "PASC920",
        "3330193392"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            36
          ]
        },
        "side": {
          "values": [
            28
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASC998_Cleveland": {
      "name": "PASC998_Cleveland",
      "aliases": [
        "PASC998_Cleveland",
        "PASC998",
        "3248404464"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD002_Sampson_1917": {
      "name": "PASD002_Sampson_1917",
      "aliases": [
        "PASD002_Sampson_1917",
        "PASD002",
        "4292753392"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD005_Farragut_1944": {
      "name": "PASD005_Farragut_1944",
      "aliases": [
        "PASD005_Farragut_1944",
        "PASD005",
        "4289607664"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD006_Mahan_1936": {
      "name": "PASD006_Mahan_1936",
      "aliases": [
        "PASD006_Mahan_1936",
        "PASD006",
        "4288559088"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD008_Benson_1945": {
      "name": "PASD008_Benson_1945",
      "aliases": [
        "PASD008_Benson_1945",
        "PASD008",
        "4286461936"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD013_Gearing_1945": {
      "name": "PASD013_Gearing_1945",
      "aliases": [
        "PASD013_Gearing_1945",
        "PASD013",
        "4281219056"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD014_Leader_1919": {
      "name": "PASD014_Leader_1919",
      "aliases": [
        "PASD014_Leader_1919",
        "PASD014",
        "4280170480"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            13
          ],
          "stern": [
            10,
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            15
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD019_Clemson_1920": {
      "name": "PASD019_Clemson_1920",
      "aliases": [
        "PASD019_Clemson_1920",
        "PASD019",
        "4274927600"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            13
          ],
          "stern": [
            10,
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD021_Fletcher_1943": {
      "name": "PASD021_Fletcher_1943",
      "aliases": [
        "PASD021_Fletcher_1943",
        "PASD021",
        "4272830448"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD027_Wickes_1918": {
      "name": "PASD027_Wickes_1918",
      "aliases": [
        "PASD027_Wickes_1918",
        "PASD027",
        "4266538992"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            10,
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD029_Sims_1941": {
      "name": "PASD029_Sims_1941",
      "aliases": [
        "PASD029_Sims_1941",
        "PASD029",
        "4264441840"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD037_Hughes": {
      "name": "PASD037_Hughes",
      "aliases": [
        "PASD037_Hughes",
        "PASD037",
        "4256053232"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": 36,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD038_Osborne": {
      "name": "PASD038_Osborne",
      "aliases": [
        "PASD038_Osborne",
        "PASD038",
        "4255004656"
      ],
      "mainGunCaliberMm": 137,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": 38,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD039_Christopher": {
      "name": "PASD039_Christopher",
      "aliases": [
        "PASD039_Christopher",
        "PASD039",
        "4253956080"
      ],
      "mainGunCaliberMm": 137,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": 38,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD040_Burrows": {
      "name": "PASD040_Burrows",
      "aliases": [
        "PASD040_Burrows",
        "PASD040",
        "4252907504"
      ],
      "mainGunCaliberMm": 137,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": 38,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD111_Joshua_Humphreys": {
      "name": "PASD111_Joshua_Humphreys",
      "aliases": [
        "PASD111_Joshua_Humphreys",
        "PASD111",
        "4178458608"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD502_Smith": {
      "name": "PASD502_Smith",
      "aliases": [
        "PASD502_Smith",
        "PASD502",
        "3768465392"
      ],
      "mainGunCaliberMm": 76.2,
      "mainGunHePenMm": 13,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD505_Hill": {
      "name": "PASD505_Hill",
      "aliases": [
        "PASD505_Hill",
        "PASD505",
        "3765319664"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD506_Monaghan": {
      "name": "PASD506_Monaghan",
      "aliases": [
        "PASD506_Monaghan",
        "PASD506",
        "3764271088"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD508_Kidd": {
      "name": "PASD508_Kidd",
      "aliases": [
        "PASD508_Kidd",
        "PASD508",
        "3762173936"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD509_Benham": {
      "name": "PASD509_Benham",
      "aliases": [
        "PASD509_Benham",
        "PASD509",
        "3761125360"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD510_Somers": {
      "name": "PASD510_Somers",
      "aliases": [
        "PASD510_Somers",
        "PASD510",
        "3760076784"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD519_Halford": {
      "name": "PASD519_Halford",
      "aliases": [
        "PASD519_Halford",
        "PASD519",
        "3750639600"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD529_Black_Black": {
      "name": "PASD529_Black_Black",
      "aliases": [
        "PASD529_Black_Black",
        "PASD529",
        "3740153840"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD597_Black_Sims": {
      "name": "PASD597_Black_Sims",
      "aliases": [
        "PASD597_Black_Sims",
        "PASD597",
        "3668850672"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD610_Forrest_Sherman": {
      "name": "PASD610_Forrest_Sherman",
      "aliases": [
        "PASD610_Forrest_Sherman",
        "PASD610",
        "3655219184"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": 36,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD704_DD_214": {
      "name": "PASD704_DD_214",
      "aliases": [
        "PASD704_DD_214",
        "PASD704",
        "3556653040"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            13
          ],
          "stern": [
            10,
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD709_Black": {
      "name": "PASD709_Black",
      "aliases": [
        "PASD709_Black",
        "PASD709",
        "3551410160"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD710_Laffey": {
      "name": "PASD710_Laffey",
      "aliases": [
        "PASD710_Laffey",
        "PASD710",
        "3550361584"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD719_Johnston": {
      "name": "PASD719_Johnston",
      "aliases": [
        "PASD719_Johnston",
        "PASD719",
        "3540924400"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": 36,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD720_Hull": {
      "name": "PASD720_Hull",
      "aliases": [
        "PASD720_Hull",
        "PASD720",
        "3539875824"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD810_TST_GEARING": {
      "name": "PASD810_TST_GEARING",
      "aliases": [
        "PASD810_TST_GEARING",
        "PASD810",
        "3445503984"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD819_FBO_Johnston": {
      "name": "PASD819_FBO_Johnston",
      "aliases": [
        "PASD819_FBO_Johnston",
        "PASD819",
        "3436066800"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": 36,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD891_Joshua_Humphreys_PLUS": {
      "name": "PASD891_Joshua_Humphreys_PLUS",
      "aliases": [
        "PASD891_Joshua_Humphreys_PLUS",
        "PASD891",
        "3360569328"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD899_Frank_Friday": {
      "name": "PASD899_Frank_Friday",
      "aliases": [
        "PASD899_Frank_Friday",
        "PASD899",
        "3352180720"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": 36,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASD913_Gearing_1945": {
      "name": "PASD913_Gearing_1945",
      "aliases": [
        "PASD913_Gearing_1945",
        "PASD913",
        "3337500656"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASS106_Cachalot": {
      "name": "PASS106_Cachalot",
      "aliases": [
        "PASS106_Cachalot",
        "PASS106",
        "4183209968"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            13,
            16,
            19
          ],
          "stern": [
            6,
            13,
            16,
            19
          ]
        },
        "deck": {
          "values": [
            6,
            13,
            16,
            19
          ]
        },
        "side": {
          "values": [
            6,
            13,
            16,
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASS108_Salmon": {
      "name": "PASS108_Salmon",
      "aliases": [
        "PASS108_Salmon",
        "PASS108",
        "4181112816"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            16,
            19,
            25
          ],
          "stern": [
            6,
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASS110_Balao": {
      "name": "PASS110_Balao",
      "aliases": [
        "PASS110_Balao",
        "PASS110",
        "4179015664"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            16,
            19,
            25
          ],
          "stern": [
            6,
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASS206_Cachalot": {
      "name": "PASS206_Cachalot",
      "aliases": [
        "PASS206_Cachalot",
        "PASS206",
        "4078352368"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            13,
            16,
            19
          ],
          "stern": [
            6,
            13,
            16,
            19
          ]
        },
        "deck": {
          "values": [
            6,
            13,
            16,
            19
          ]
        },
        "side": {
          "values": [
            6,
            13,
            16,
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASS208_Salmon": {
      "name": "PASS208_Salmon",
      "aliases": [
        "PASS208_Salmon",
        "PASS208",
        "4076255216"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            16,
            19,
            25
          ],
          "stern": [
            6,
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASS210_Balao": {
      "name": "PASS210_Balao",
      "aliases": [
        "PASS210_Balao",
        "PASS210",
        "4074158064"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            16,
            19,
            25
          ],
          "stern": [
            6,
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASS510_Gato": {
      "name": "PASS510_Gato",
      "aliases": [
        "PASS510_Gato",
        "PASS510",
        "3759585264"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            16,
            19,
            25
          ],
          "stern": [
            6,
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASS710_Archerfish": {
      "name": "PASS710_Archerfish",
      "aliases": [
        "PASS710_Archerfish",
        "PASS710",
        "3549870064"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 36,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            16,
            19,
            25
          ],
          "stern": [
            6,
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASS910_Balao_2": {
      "name": "PASS910_Balao_2",
      "aliases": [
        "PASS910_Balao_2",
        "PASS910",
        "3340154864"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            16,
            19,
            25
          ],
          "stern": [
            6,
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASX001_Cimarron": {
      "name": "PASX001_Cimarron",
      "aliases": [
        "PASX001_Cimarron",
        "PASX001",
        "4293146608"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            14
          ],
          "stern": [
            10,
            13,
            14
          ]
        },
        "deck": {
          "values": [
            14
          ]
        },
        "side": {
          "values": [
            18
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASX003_Liberty": {
      "name": "PASX003_Liberty",
      "aliases": [
        "PASX003_Liberty",
        "PASX003",
        "4291049456"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            14
          ],
          "stern": [
            10,
            13
          ]
        },
        "deck": {
          "values": [
            14
          ]
        },
        "side": {
          "values": [
            18
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASX004_Liberty_modern": {
      "name": "PASX004_Liberty_modern",
      "aliases": [
        "PASX004_Liberty_modern",
        "PASX004",
        "4290000880"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            14
          ],
          "stern": [
            10,
            13
          ]
        },
        "deck": {
          "values": [
            14
          ]
        },
        "side": {
          "values": [
            18
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASX005_St_Clair": {
      "name": "PASX005_St_Clair",
      "aliases": [
        "PASX005_St_Clair",
        "PASX005",
        "4288952304"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13,
            14
          ],
          "stern": [
            13,
            14
          ]
        },
        "deck": {
          "values": [
            14
          ]
        },
        "side": {
          "values": [
            18
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PASX904_Cimarron": {
      "name": "PASX904_Cimarron",
      "aliases": [
        "PASX904_Cimarron",
        "PASX904",
        "3346282480"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            12
          ],
          "stern": [
            12
          ]
        },
        "deck": {
          "values": []
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSA106_Furious": {
      "name": "PBSA106_Furious",
      "aliases": [
        "PBSA106_Furious",
        "PBSA106",
        "4183799760"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            13,
            19
          ]
        },
        "deck": {
          "values": [
            21
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSA108_Implacable": {
      "name": "PBSA108_Implacable",
      "aliases": [
        "PBSA108_Implacable",
        "PBSA108",
        "4181702608"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            25
          ],
          "stern": [
            19,
            21
          ]
        },
        "deck": {
          "values": [
            21,
            25,
            38,
            76
          ]
        },
        "side": {
          "values": [
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSA111_Eagle": {
      "name": "PBSA111_Eagle",
      "aliases": [
        "PBSA111_Eagle",
        "PBSA111",
        "4178556880"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            21,
            25
          ],
          "stern": [
            21,
            25
          ]
        },
        "deck": {
          "values": [
            38,
            102
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSA204_Hermes": {
      "name": "PBSA204_Hermes",
      "aliases": [
        "PBSA204_Hermes",
        "PBSA204",
        "4081039312"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            25
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            76
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            76
          ],
          "bow": [
            76
          ],
          "stern": [
            76
          ]
        }
      }
    },
    "PBSA210_Audacious": {
      "name": "PBSA210_Audacious",
      "aliases": [
        "PBSA210_Audacious",
        "PBSA210",
        "4074747856"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            21,
            25
          ],
          "stern": [
            21,
            25
          ]
        },
        "deck": {
          "values": [
            38,
            102
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSA508_Indomitable": {
      "name": "PBSA508_Indomitable",
      "aliases": [
        "PBSA508_Indomitable",
        "PBSA508",
        "3762272208"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            21,
            25
          ],
          "stern": [
            21,
            25
          ]
        },
        "deck": {
          "values": [
            25,
            38,
            76
          ]
        },
        "side": {
          "values": [
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSA510_Malta": {
      "name": "PBSA510_Malta",
      "aliases": [
        "PBSA510_Malta",
        "PBSA510",
        "3760175056"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            21
          ],
          "stern": [
            21
          ]
        },
        "deck": {
          "values": [
            21,
            38,
            102
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSA518_Ark_Royal": {
      "name": "PBSA518_Ark_Royal",
      "aliases": [
        "PBSA518_Ark_Royal",
        "PBSA518",
        "3751786448"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSA528_Colossus": {
      "name": "PBSA528_Colossus",
      "aliases": [
        "PBSA528_Colossus",
        "PBSA528",
        "3741300688"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            25
          ],
          "stern": [
            19,
            25
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            19,
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSA710_Ocean": {
      "name": "PBSA710_Ocean",
      "aliases": [
        "PBSA710_Ocean",
        "PBSA710",
        "3550459856"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            30
          ],
          "stern": [
            19,
            25,
            30
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            19,
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSA718_Theseus": {
      "name": "PBSA718_Theseus",
      "aliases": [
        "PBSA718_Theseus",
        "PBSA718",
        "3542071248"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            25
          ],
          "stern": [
            19,
            25
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            19,
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSA910_TST_Audacious": {
      "name": "PBSA910_TST_Audacious",
      "aliases": [
        "PBSA910_TST_Audacious",
        "PBSA910",
        "3340744656"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            21,
            25
          ],
          "stern": [
            21,
            25
          ]
        },
        "deck": {
          "values": [
            38,
            102
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB002_Warspite_1941": {
      "name": "PBSB002_Warspite_1941",
      "aliases": [
        "PBSB002_Warspite_1941",
        "PBSB002",
        "4292818896"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26,
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            102,
            152
          ],
          "bow": [
            102,
            152
          ],
          "stern": [
            102,
            152
          ]
        }
      }
    },
    "PBSB103_Bellerophon": {
      "name": "PBSB103_Bellerophon",
      "aliases": [
        "PBSB103_Bellerophon",
        "PBSB103",
        "4186912720"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            203
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            152,
            178
          ],
          "bow": [
            152,
            178
          ],
          "stern": []
        }
      }
    },
    "PBSB104_Orion": {
      "name": "PBSB104_Orion",
      "aliases": [
        "PBSB104_Orion",
        "PBSB104",
        "4185864144"
      ],
      "mainGunCaliberMm": 343,
      "mainGunHePenMm": 86,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            203
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB105_Iron_Duke": {
      "name": "PBSB105_Iron_Duke",
      "aliases": [
        "PBSB105_Iron_Duke",
        "PBSB105",
        "4184815568"
      ],
      "mainGunCaliberMm": 343,
      "mainGunHePenMm": 86,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            203,
            229
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            102,
            152
          ],
          "bow": [
            102,
            152
          ],
          "stern": [
            102,
            152
          ]
        }
      }
    },
    "PBSB106_Queen_Elizabeth": {
      "name": "PBSB106_Queen_Elizabeth",
      "aliases": [
        "PBSB106_Queen_Elizabeth",
        "PBSB106",
        "4183766992"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            102,
            152
          ],
          "bow": [
            102,
            152
          ],
          "stern": [
            102,
            152
          ]
        }
      }
    },
    "PBSB107_King_George_V": {
      "name": "PBSB107_King_George_V",
      "aliases": [
        "PBSB107_King_George_V",
        "PBSB107",
        "4182718416"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 89,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26,
            356,
            381
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB108_Monarch": {
      "name": "PBSB108_Monarch",
      "aliases": [
        "PBSB108_Monarch",
        "PBSB108",
        "4181669840"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32,
            356,
            381
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB109_Lion": {
      "name": "PBSB109_Lion",
      "aliases": [
        "PBSB109_Lion",
        "PBSB109",
        "4180621264"
      ],
      "mainGunCaliberMm": 419,
      "mainGunHePenMm": 105,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32,
            381
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB110_Conqueror": {
      "name": "PBSB110_Conqueror",
      "aliases": [
        "PBSB110_Conqueror",
        "PBSB110",
        "4179572688"
      ],
      "mainGunCaliberMm": 419,
      "mainGunHePenMm": 105,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32,
            406
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB111_Devastation": {
      "name": "PBSB111_Devastation",
      "aliases": [
        "PBSB111_Devastation",
        "PBSB111",
        "4178524112"
      ],
      "mainGunCaliberMm": 419,
      "mainGunHePenMm": 105,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32,
            432
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB203_Indefatigable": {
      "name": "PBSB203_Indefatigable",
      "aliases": [
        "PBSB203_Indefatigable",
        "PBSB203",
        "4082055120"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            64
          ],
          "bow": [
            64
          ],
          "stern": []
        }
      }
    },
    "PBSB204_Queen_Mary": {
      "name": "PBSB204_Queen_Mary",
      "aliases": [
        "PBSB204_Queen_Mary",
        "PBSB204",
        "4081006544"
      ],
      "mainGunCaliberMm": 343,
      "mainGunHePenMm": 57,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            76
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            102
          ],
          "bow": [
            102
          ],
          "stern": []
        }
      }
    },
    "PBSB205_Tiger": {
      "name": "PBSB205_Tiger",
      "aliases": [
        "PBSB205_Tiger",
        "PBSB205",
        "4079957968"
      ],
      "mainGunCaliberMm": 343,
      "mainGunHePenMm": 57,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            25
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            102,
            127
          ],
          "bow": [
            102,
            127
          ],
          "stern": [
            102
          ]
        }
      }
    },
    "PBSB206_Renown": {
      "name": "PBSB206_Renown",
      "aliases": [
        "PBSB206_Renown",
        "PBSB206",
        "4078909392"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            29
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB207_Rooke": {
      "name": "PBSB207_Rooke",
      "aliases": [
        "PBSB207_Rooke",
        "PBSB207",
        "4077860816"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            305
          ],
          "bow": [
            305
          ],
          "stern": [
            305
          ]
        }
      }
    },
    "PBSB208_Hawke": {
      "name": "PBSB208_Hawke",
      "aliases": [
        "PBSB208_Hawke",
        "PBSB208",
        "4076812240"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB209_Duncan": {
      "name": "PBSB209_Duncan",
      "aliases": [
        "PBSB209_Duncan",
        "PBSB209",
        "4075763664"
      ],
      "mainGunCaliberMm": 419,
      "mainGunHePenMm": 70,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB210_St_Vincent": {
      "name": "PBSB210_St_Vincent",
      "aliases": [
        "PBSB210_St_Vincent",
        "PBSB210",
        "4074715088"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB503_Dreadnought": {
      "name": "PBSB503_Dreadnought",
      "aliases": [
        "PBSB503_Dreadnought",
        "PBSB503",
        "3767482320"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            152
          ],
          "bow": [
            152
          ],
          "stern": []
        }
      }
    },
    "PBSB505_Agincourt": {
      "name": "PBSB505_Agincourt",
      "aliases": [
        "PBSB505_Agincourt",
        "PBSB505",
        "3765385168"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            38
          ],
          "stern": [
            19,
            38
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            152,
            229
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            102
          ],
          "bow": [
            102
          ],
          "stern": [
            102
          ]
        }
      }
    },
    "PBSB507_Hood": {
      "name": "PBSB507_Hood",
      "aliases": [
        "PBSB507_Hood",
        "PBSB507",
        "3763288016"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            51
          ]
        },
        "side": {
          "values": [
            127,
            178
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            127
          ],
          "bow": [
            127
          ],
          "stern": []
        }
      }
    },
    "PBSB508_Vanguard": {
      "name": "PBSB508_Vanguard",
      "aliases": [
        "PBSB508_Vanguard",
        "PBSB508",
        "3762239440"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32,
            343,
            356
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB509_Marlborough": {
      "name": "PBSB509_Marlborough",
      "aliases": [
        "PBSB509_Marlborough",
        "PBSB509",
        "3761190864"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 89,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB510_Thunderer": {
      "name": "PBSB510_Thunderer",
      "aliases": [
        "PBSB510_Thunderer",
        "PBSB510",
        "3760142288"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 114,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32,
            406
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB517_Nelson": {
      "name": "PBSB517_Nelson",
      "aliases": [
        "PBSB517_Nelson",
        "PBSB517",
        "3752802256"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 102,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26,
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB526_Repulse": {
      "name": "PBSB526_Repulse",
      "aliases": [
        "PBSB526_Repulse",
        "PBSB526",
        "3743365072"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            38,
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            152
          ],
          "bow": [
            152
          ],
          "stern": []
        }
      }
    },
    "PBSB527_Duke_of_York": {
      "name": "PBSB527_Duke_of_York",
      "aliases": [
        "PBSB527_Duke_of_York",
        "PBSB527",
        "3742316496"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 89,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26,
            356,
            381
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB536_Black_Repulse": {
      "name": "PBSB536_Black_Repulse",
      "aliases": [
        "PBSB536_Black_Repulse",
        "PBSB536",
        "3732879312"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            38,
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            152
          ],
          "bow": [
            152
          ],
          "stern": []
        }
      }
    },
    "PBSB537_Collingwood": {
      "name": "PBSB537_Collingwood",
      "aliases": [
        "PBSB537_Collingwood",
        "PBSB537",
        "3731830736"
      ],
      "mainGunCaliberMm": 419,
      "mainGunHePenMm": 70,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB547_Renown_1944": {
      "name": "PBSB547_Renown_1944",
      "aliases": [
        "PBSB547_Renown_1944",
        "PBSB547",
        "3721344976"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            29
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB609_Scarlet_Thunder": {
      "name": "PBSB609_Scarlet_Thunder",
      "aliases": [
        "PBSB609_Scarlet_Thunder",
        "PBSB609",
        "3656333264"
      ],
      "mainGunCaliberMm": 419,
      "mainGunHePenMm": 105,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB610_Incomparable": {
      "name": "PBSB610_Incomparable",
      "aliases": [
        "PBSB610_Incomparable",
        "PBSB610",
        "3655284688"
      ],
      "mainGunCaliberMm": 508,
      "mainGunHePenMm": 85,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            51
          ]
        },
        "side": {
          "values": [
            102,
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            102
          ],
          "bow": [
            102
          ],
          "stern": []
        }
      }
    },
    "PBSB708_Prince_of_Wales": {
      "name": "PBSB708_Prince_of_Wales",
      "aliases": [
        "PBSB708_Prince_of_Wales",
        "PBSB708",
        "3552524240"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 89,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32,
            356,
            381
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB717_Rodney": {
      "name": "PBSB717_Rodney",
      "aliases": [
        "PBSB717_Rodney",
        "PBSB717",
        "3543087056"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26,
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB727_Duke_of_Bronte": {
      "name": "PBSB727_Duke_of_Bronte",
      "aliases": [
        "PBSB727_Duke_of_Bronte",
        "PBSB727",
        "3532601296"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26,
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB737_Royal_Sovereign": {
      "name": "PBSB737_Royal_Sovereign",
      "aliases": [
        "PBSB737_Royal_Sovereign",
        "PBSB737",
        "3522115536"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            152
          ],
          "bow": [
            152
          ],
          "stern": [
            152
          ]
        }
      }
    },
    "PBSB747_STPatric_Duke_of_York": {
      "name": "PBSB747_STPatric_Duke_of_York",
      "aliases": [
        "PBSB747_STPatric_Duke_of_York",
        "PBSB747",
        "3511629776"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 89,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26,
            356,
            381
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB810_Cumberland": {
      "name": "PBSB810_Cumberland",
      "aliases": [
        "PBSB810_Cumberland",
        "PBSB810",
        "3445569488"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB910_Conqueror": {
      "name": "PBSB910_Conqueror",
      "aliases": [
        "PBSB910_Conqueror",
        "PBSB910",
        "3340711888"
      ],
      "mainGunCaliberMm": 419,
      "mainGunHePenMm": 105,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32,
            406
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSB998_St_Lawrence": {
      "name": "PBSB998_St_Lawrence",
      "aliases": [
        "PBSB998_St_Lawrence",
        "PBSB998",
        "3248437200"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 114,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC020_Monmouth": {
      "name": "PBSC020_Monmouth",
      "aliases": [
        "PBSC020_Monmouth",
        "PBSC020",
        "4273911760"
      ],
      "mainGunCaliberMm": 234,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC101_Black_Swan": {
      "name": "PBSC101_Black_Swan",
      "aliases": [
        "PBSC101_Black_Swan",
        "PBSC101",
        "4188977104"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10,
            13
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC102_Weymouth": {
      "name": "PBSC102_Weymouth",
      "aliases": [
        "PBSC102_Weymouth",
        "PBSC102",
        "4187928528"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC103_Caledon": {
      "name": "PBSC103_Caledon",
      "aliases": [
        "PBSC103_Caledon",
        "PBSC103",
        "4186879952"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            38,
            57,
            76
          ],
          "bow": [
            38,
            57,
            76
          ],
          "stern": [
            57,
            76
          ]
        }
      }
    },
    "PBSC104_Danae": {
      "name": "PBSC104_Danae",
      "aliases": [
        "PBSC104_Danae",
        "PBSC104",
        "4185831376"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            38,
            57,
            76
          ],
          "bow": [
            38,
            57,
            76
          ],
          "stern": [
            57,
            76
          ]
        }
      }
    },
    "PBSC105_Emerald": {
      "name": "PBSC105_Emerald",
      "aliases": [
        "PBSC105_Emerald",
        "PBSC105",
        "4184782800"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            38,
            57,
            76
          ],
          "bow": [
            38,
            57,
            76
          ],
          "stern": [
            57,
            76
          ]
        }
      }
    },
    "PBSC106_Leander": {
      "name": "PBSC106_Leander",
      "aliases": [
        "PBSC106_Leander",
        "PBSC106",
        "4183734224"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC107_Fiji": {
      "name": "PBSC107_Fiji",
      "aliases": [
        "PBSC107_Fiji",
        "PBSC107",
        "4182685648"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC108_Edinburgh": {
      "name": "PBSC108_Edinburgh",
      "aliases": [
        "PBSC108_Edinburgh",
        "PBSC108",
        "4181637072"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC109_Neptune": {
      "name": "PBSC109_Neptune",
      "aliases": [
        "PBSC109_Neptune",
        "PBSC109",
        "4180588496"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16,
            76
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC110_Minotaur": {
      "name": "PBSC110_Minotaur",
      "aliases": [
        "PBSC110_Minotaur",
        "PBSC110",
        "4179539920"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC111_Edgar": {
      "name": "PBSC111_Edgar",
      "aliases": [
        "PBSC111_Edgar",
        "PBSC111",
        "4178491344"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16,
            102
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC205_Hawkins": {
      "name": "PBSC205_Hawkins",
      "aliases": [
        "PBSC205_Hawkins",
        "PBSC205",
        "4079925200"
      ],
      "mainGunCaliberMm": 190,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            51
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            38,
            57
          ],
          "bow": [
            38
          ],
          "stern": [
            57
          ]
        }
      }
    },
    "PBSC206_Devonshire": {
      "name": "PBSC206_Devonshire",
      "aliases": [
        "PBSC206_Devonshire",
        "PBSC206",
        "4078876624"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC207_Surrey": {
      "name": "PBSC207_Surrey",
      "aliases": [
        "PBSC207_Surrey",
        "PBSC207",
        "4077828048"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC208_Albemarle": {
      "name": "PBSC208_Albemarle",
      "aliases": [
        "PBSC208_Albemarle",
        "PBSC208",
        "4076779472"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25,
            76
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC209_Drake": {
      "name": "PBSC209_Drake",
      "aliases": [
        "PBSC209_Drake",
        "PBSC209",
        "4075730896"
      ],
      "mainGunCaliberMm": 234,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC210_Goliath": {
      "name": "PBSC210_Goliath",
      "aliases": [
        "PBSC210_Goliath",
        "PBSC210",
        "4074682320"
      ],
      "mainGunCaliberMm": 234,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC505_Exeter": {
      "name": "PBSC505_Exeter",
      "aliases": [
        "PBSC505_Exeter",
        "PBSC505",
        "3765352400"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC507_Belfast_1959": {
      "name": "PBSC507_Belfast_1959",
      "aliases": [
        "PBSC507_Belfast_1959",
        "PBSC507",
        "3763255248"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC508_Cheshire": {
      "name": "PBSC508_Cheshire",
      "aliases": [
        "PBSC508_Cheshire",
        "PBSC508",
        "3762206672"
      ],
      "mainGunCaliberMm": 234,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25,
            76
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC510_Plymouth": {
      "name": "PBSC510_Plymouth",
      "aliases": [
        "PBSC510_Plymouth",
        "PBSC510",
        "3760109520"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19,
            114
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC516_London": {
      "name": "PBSC516_London",
      "aliases": [
        "PBSC516_London",
        "PBSC516",
        "3753818064"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC518_Tiger_1959": {
      "name": "PBSC518_Tiger_1959",
      "aliases": [
        "PBSC518_Tiger_1959",
        "PBSC518",
        "3751720912"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC526_Dido": {
      "name": "PBSC526_Dido",
      "aliases": [
        "PBSC526_Dido",
        "PBSC526",
        "3743332304"
      ],
      "mainGunCaliberMm": 133,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13,
            25
          ]
        },
        "side": {
          "values": [
            13,
            89
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC528_Belfast_1943": {
      "name": "PBSC528_Belfast_1943",
      "aliases": [
        "PBSC528_Belfast_1943",
        "PBSC528",
        "3741235152"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC538_Hampshire": {
      "name": "PBSC538_Hampshire",
      "aliases": [
        "PBSC538_Hampshire",
        "PBSC538",
        "3730749392"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC548_Nottingham": {
      "name": "PBSC548_Nottingham",
      "aliases": [
        "PBSC548_Nottingham",
        "PBSC548",
        "3720263632"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC558_AZUR_Cheshire": {
      "name": "PBSC558_AZUR_Cheshire",
      "aliases": [
        "PBSC558_AZUR_Cheshire",
        "PBSC558",
        "3709777872"
      ],
      "mainGunCaliberMm": 234,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25,
            76
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC610_Gibraltar": {
      "name": "PBSC610_Gibraltar",
      "aliases": [
        "PBSC610_Gibraltar",
        "PBSC610",
        "3655251920"
      ],
      "mainGunCaliberMm": 234,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC707_STPatric_Belfast_1959": {
      "name": "PBSC707_STPatric_Belfast_1959",
      "aliases": [
        "PBSC707_STPatric_Belfast_1959",
        "PBSC707",
        "3553540048"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC708_STPatric_Belfast_1943": {
      "name": "PBSC708_STPatric_Belfast_1943",
      "aliases": [
        "PBSC708_STPatric_Belfast_1943",
        "PBSC708",
        "3552491472"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC716_Orion_1944": {
      "name": "PBSC716_Orion_1944",
      "aliases": [
        "PBSC716_Orion_1944",
        "PBSC716",
        "3544102864"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC718_STPatric_Tiger_1959": {
      "name": "PBSC718_STPatric_Tiger_1959",
      "aliases": [
        "PBSC718_STPatric_Tiger_1959",
        "PBSC718",
        "3542005712"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC719_Aberdeen": {
      "name": "PBSC719_Aberdeen",
      "aliases": [
        "PBSC719_Aberdeen",
        "PBSC719",
        "3540957136"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC810_Defence": {
      "name": "PBSC810_Defence",
      "aliases": [
        "PBSC810_Defence",
        "PBSC810",
        "3445536720"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 89,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC888_Edinburgh_PR": {
      "name": "PBSC888_Edinburgh_PR",
      "aliases": [
        "PBSC888_Edinburgh_PR",
        "PBSC888",
        "3363747792"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC909_Pirate_Neptune": {
      "name": "PBSC909_Pirate_Neptune",
      "aliases": [
        "PBSC909_Pirate_Neptune",
        "PBSC909",
        "3341727696"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16,
            76
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC910_Cyclops": {
      "name": "PBSC910_Cyclops",
      "aliases": [
        "PBSC910_Cyclops",
        "PBSC910",
        "3340679120"
      ],
      "mainGunCaliberMm": 234,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSC920_Pirate_Plymouth": {
      "name": "PBSC920_Pirate_Plymouth",
      "aliases": [
        "PBSC920_Pirate_Plymouth",
        "PBSC920",
        "3330193360"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19,
            114
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD102_Medea": {
      "name": "PBSD102_Medea",
      "aliases": [
        "PBSD102_Medea",
        "PBSD102",
        "4187895760"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD103_Valkyrie": {
      "name": "PBSD103_Valkyrie",
      "aliases": [
        "PBSD103_Valkyrie",
        "PBSD103",
        "4186847184"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD104_Wakeful": {
      "name": "PBSD104_Wakeful",
      "aliases": [
        "PBSD104_Wakeful",
        "PBSD104",
        "4185798608"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD105_Acasta": {
      "name": "PBSD105_Acasta",
      "aliases": [
        "PBSD105_Acasta",
        "PBSD105",
        "4184750032"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD106_Icarus": {
      "name": "PBSD106_Icarus",
      "aliases": [
        "PBSD106_Icarus",
        "PBSD106",
        "4183701456"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD107_Jervis": {
      "name": "PBSD107_Jervis",
      "aliases": [
        "PBSD107_Jervis",
        "PBSD107",
        "4182652880"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD108_Lightning": {
      "name": "PBSD108_Lightning",
      "aliases": [
        "PBSD108_Lightning",
        "PBSD108",
        "4181604304"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD109_Jutland": {
      "name": "PBSD109_Jutland",
      "aliases": [
        "PBSD109_Jutland",
        "PBSD109",
        "4180555728"
      ],
      "mainGunCaliberMm": 113,
      "mainGunHePenMm": 19,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD110_Daring": {
      "name": "PBSD110_Daring",
      "aliases": [
        "PBSD110_Daring",
        "PBSD110",
        "4179507152"
      ],
      "mainGunCaliberMm": 113,
      "mainGunHePenMm": 19,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD503_Campbeltown_1941": {
      "name": "PBSD503_Campbeltown_1941",
      "aliases": [
        "PBSD503_Campbeltown_1941",
        "PBSD503",
        "3767416784"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            10,
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD506_Gallant": {
      "name": "PBSD506_Gallant",
      "aliases": [
        "PBSD506_Gallant",
        "PBSD506",
        "3764271056"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD510_Druid": {
      "name": "PBSD510_Druid",
      "aliases": [
        "PBSD510_Druid",
        "PBSD510",
        "3760076752"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD517_Cossack": {
      "name": "PBSD517_Cossack",
      "aliases": [
        "PBSD517_Cossack",
        "PBSD517",
        "3752736720"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD519_Somme": {
      "name": "PBSD519_Somme",
      "aliases": [
        "PBSD519_Somme",
        "PBSD519",
        "3750639568"
      ],
      "mainGunCaliberMm": 113,
      "mainGunHePenMm": 19,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD598_Black_Cossack": {
      "name": "PBSD598_Black_Cossack",
      "aliases": [
        "PBSD598_Black_Cossack",
        "PBSD598",
        "3667802064"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD605_Anthony_Event": {
      "name": "PBSD605_Anthony_Event",
      "aliases": [
        "PBSD605_Anthony_Event",
        "PBSD605",
        "3660462032"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            16
          ],
          "stern": [
            10,
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD717_Jupiter_1942": {
      "name": "PBSD717_Jupiter_1942",
      "aliases": [
        "PBSD717_Jupiter_1942",
        "PBSD717",
        "3543021520"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD718_Eskimo": {
      "name": "PBSD718_Eskimo",
      "aliases": [
        "PBSD718_Eskimo",
        "PBSD718",
        "3541972944"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSD719_Barfleur": {
      "name": "PBSD719_Barfleur",
      "aliases": [
        "PBSD719_Barfleur",
        "PBSD719",
        "3540924368"
      ],
      "mainGunCaliberMm": 113,
      "mainGunHePenMm": 19,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSS106_Undine": {
      "name": "PBSS106_Undine",
      "aliases": [
        "PBSS106_Undine",
        "PBSS106",
        "4183209936"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSS108_Sturdy": {
      "name": "PBSS108_Sturdy",
      "aliases": [
        "PBSS108_Sturdy",
        "PBSS108",
        "4181112784"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSS110_Thrasher": {
      "name": "PBSS110_Thrasher",
      "aliases": [
        "PBSS110_Thrasher",
        "PBSS110",
        "4179015632"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 29.5,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSS508_Alliance": {
      "name": "PBSS508_Alliance",
      "aliases": [
        "PBSS508_Alliance",
        "PBSS508",
        "3761682384"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSS710_Seal": {
      "name": "PBSS710_Seal",
      "aliases": [
        "PBSS710_Seal",
        "PBSS710",
        "3549870032"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 29.5,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PBSS910_Selkie": {
      "name": "PBSS910_Selkie",
      "aliases": [
        "PBSS910_Selkie",
        "PBSS910",
        "3340154832"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 29.5,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            16,
            19,
            25
          ],
          "stern": [
            6,
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSA506_Bearn": {
      "name": "PFSA506_Bearn",
      "aliases": [
        "PFSA506_Bearn",
        "PFSA506",
        "3764369232"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19
          ],
          "stern": [
            16,
            19,
            24
          ]
        },
        "deck": {
          "values": [
            24
          ]
        },
        "side": {
          "values": [
            83
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            83
          ],
          "bow": [
            83
          ],
          "stern": [
            83
          ]
        }
      }
    },
    "PFSB103_Turenne": {
      "name": "PFSB103_Turenne",
      "aliases": [
        "PFSB103_Turenne",
        "PFSB103",
        "4186912592"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            100
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB104_Courbet": {
      "name": "PFSB104_Courbet",
      "aliases": [
        "PFSB104_Courbet",
        "PFSB104",
        "4185864016"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19,
            40
          ]
        },
        "side": {
          "values": [
            160
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            150,
            200
          ],
          "bow": [
            150,
            200
          ],
          "stern": [
            150,
            200
          ]
        }
      }
    },
    "PFSB105_Bretagne": {
      "name": "PFSB105_Bretagne",
      "aliases": [
        "PFSB105_Bretagne",
        "PFSB105",
        "4184815440"
      ],
      "mainGunCaliberMm": 340,
      "mainGunHePenMm": 57,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19,
            30
          ]
        },
        "side": {
          "values": [
            160
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB106_Normandie": {
      "name": "PFSB106_Normandie",
      "aliases": [
        "PFSB106_Normandie",
        "PFSB106",
        "4183766864"
      ],
      "mainGunCaliberMm": 340,
      "mainGunHePenMm": 57,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26,
            30
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            180
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            120,
            180
          ],
          "bow": [
            180
          ],
          "stern": [
            120
          ]
        }
      }
    },
    "PFSB107_Lyon": {
      "name": "PFSB107_Lyon",
      "aliases": [
        "PFSB107_Lyon",
        "PFSB107",
        "4182718288"
      ],
      "mainGunCaliberMm": 340,
      "mainGunHePenMm": 57,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            12,
            26
          ],
          "stern": [
            26,
            30
          ]
        },
        "deck": {
          "values": [
            26,
            30
          ]
        },
        "side": {
          "values": [
            180
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            120,
            180
          ],
          "bow": [
            180
          ],
          "stern": [
            120
          ]
        }
      }
    },
    "PFSB108_Richelieu": {
      "name": "PFSB108_Richelieu",
      "aliases": [
        "PFSB108_Richelieu",
        "PFSB108",
        "4181669712"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 63,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            20,
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB109_Alsace": {
      "name": "PFSB109_Alsace",
      "aliases": [
        "PFSB109_Alsace",
        "PFSB109",
        "4180621136"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 63,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB110_France": {
      "name": "PFSB110_France",
      "aliases": [
        "PFSB110_France",
        "PFSB110",
        "4179572560"
      ],
      "mainGunCaliberMm": 431,
      "mainGunHePenMm": 72,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB111_Patrie": {
      "name": "PFSB111_Patrie",
      "aliases": [
        "PFSB111_Patrie",
        "PFSB111",
        "4178523984"
      ],
      "mainGunCaliberMm": 431,
      "mainGunHePenMm": 72,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB506_Dunkerque_1940": {
      "name": "PFSB506_Dunkerque_1940",
      "aliases": [
        "PFSB506_Dunkerque_1940",
        "PFSB506",
        "3764336464"
      ],
      "mainGunCaliberMm": 330,
      "mainGunHePenMm": 55,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            20,
            26
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB507_Strasbourg": {
      "name": "PFSB507_Strasbourg",
      "aliases": [
        "PFSB507_Strasbourg",
        "PFSB507",
        "3763287888"
      ],
      "mainGunCaliberMm": 330,
      "mainGunHePenMm": 55,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            20,
            26
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB508_Gascogne": {
      "name": "PFSB508_Gascogne",
      "aliases": [
        "PFSB508_Gascogne",
        "PFSB508",
        "3762239312"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 63,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB510_Bourgogne": {
      "name": "PFSB510_Bourgogne",
      "aliases": [
        "PFSB510_Bourgogne",
        "PFSB510",
        "3760142160"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 63,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB518_Jean_Bart": {
      "name": "PFSB518_Jean_Bart",
      "aliases": [
        "PFSB518_Jean_Bart",
        "PFSB518",
        "3751753552"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 63,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            20,
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB528_Champagne": {
      "name": "PFSB528_Champagne",
      "aliases": [
        "PFSB528_Champagne",
        "PFSB528",
        "3741267792"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB538_Flandre": {
      "name": "PFSB538_Flandre",
      "aliases": [
        "PFSB538_Flandre",
        "PFSB538",
        "3730782032"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 63,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB548_Picardie": {
      "name": "PFSB548_Picardie",
      "aliases": [
        "PFSB548_Picardie",
        "PFSB548",
        "3720296272"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            12,
            32
          ],
          "stern": [
            30,
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            180
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            120,
            180
          ],
          "bow": [
            180
          ],
          "stern": [
            120
          ]
        }
      }
    },
    "PFSB596_Black_Dunkerque": {
      "name": "PFSB596_Black_Dunkerque",
      "aliases": [
        "PFSB596_Black_Dunkerque",
        "PFSB596",
        "3669964624"
      ],
      "mainGunCaliberMm": 330,
      "mainGunHePenMm": 55,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            20,
            26
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB599_Black_Jean_Bart": {
      "name": "PFSB599_Black_Jean_Bart",
      "aliases": [
        "PFSB599_Black_Jean_Bart",
        "PFSB599",
        "3666818896"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 63,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            20,
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB709_Roussillon": {
      "name": "PFSB709_Roussillon",
      "aliases": [
        "PFSB709_Roussillon",
        "PFSB709",
        "3551475536"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB898_Richelieu_coop": {
      "name": "PFSB898_Richelieu_coop",
      "aliases": [
        "PFSB898_Richelieu_coop",
        "PFSB898",
        "3353294672"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 63,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            20,
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB908_Azur_Richelieu": {
      "name": "PFSB908_Azur_Richelieu",
      "aliases": [
        "PFSB908_Azur_Richelieu",
        "PFSB908",
        "3342808912"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 63,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            20,
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSB909_Pirate_Jean_Bart": {
      "name": "PFSB909_Pirate_Jean_Bart",
      "aliases": [
        "PFSB909_Pirate_Jean_Bart",
        "PFSB909",
        "3341760336"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 63,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            20,
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC101_Bougainville": {
      "name": "PFSC101_Bougainville",
      "aliases": [
        "PFSC101_Bougainville",
        "PFSC101",
        "4188976976"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC102_Jurien": {
      "name": "PFSC102_Jurien",
      "aliases": [
        "PFSC102_Jurien",
        "PFSC102",
        "4187928400"
      ],
      "mainGunCaliberMm": 165,
      "mainGunHePenMm": 28,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC103_Friant": {
      "name": "PFSC103_Friant",
      "aliases": [
        "PFSC103_Friant",
        "PFSC103",
        "4186879824"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC104_Duguay_Trouin": {
      "name": "PFSC104_Duguay_Trouin",
      "aliases": [
        "PFSC104_Duguay_Trouin",
        "PFSC104",
        "4185831248"
      ],
      "mainGunCaliberMm": 155,
      "mainGunHePenMm": 26,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC105_Emile_Bertin": {
      "name": "PFSC105_Emile_Bertin",
      "aliases": [
        "PFSC105_Emile_Bertin",
        "PFSC105",
        "4184782672"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC106_La_Galissonniere": {
      "name": "PFSC106_La_Galissonniere",
      "aliases": [
        "PFSC106_La_Galissonniere",
        "PFSC106",
        "4183734096"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC107_Algerie": {
      "name": "PFSC107_Algerie",
      "aliases": [
        "PFSC107_Algerie",
        "PFSC107",
        "4182685520"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC108_Charles_Martel": {
      "name": "PFSC108_Charles_Martel",
      "aliases": [
        "PFSC108_Charles_Martel",
        "PFSC108",
        "4181636944"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC109_Saint_Louis": {
      "name": "PFSC109_Saint_Louis",
      "aliases": [
        "PFSC109_Saint_Louis",
        "PFSC109",
        "4180588368"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC110_Henri_IV": {
      "name": "PFSC110_Henri_IV",
      "aliases": [
        "PFSC110_Henri_IV",
        "PFSC110",
        "4179539792"
      ],
      "mainGunCaliberMm": 240,
      "mainGunHePenMm": 40,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC111_Conde": {
      "name": "PFSC111_Conde",
      "aliases": [
        "PFSC111_Conde",
        "PFSC111",
        "4178491216"
      ],
      "mainGunCaliberMm": 240,
      "mainGunHePenMm": 40,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC208_Cherbourg": {
      "name": "PFSC208_Cherbourg",
      "aliases": [
        "PFSC208_Cherbourg",
        "PFSC208",
        "4076779344"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC209_Brest": {
      "name": "PFSC209_Brest",
      "aliases": [
        "PFSC209_Brest",
        "PFSC209",
        "4075730768"
      ],
      "mainGunCaliberMm": 330,
      "mainGunHePenMm": 55,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC210_Marseille": {
      "name": "PFSC210_Marseille",
      "aliases": [
        "PFSC210_Marseille",
        "PFSC210",
        "4074682192"
      ],
      "mainGunCaliberMm": 330,
      "mainGunHePenMm": 55,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25,
            30
          ]
        },
        "deck": {
          "values": [
            36
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC506_De_Grasse": {
      "name": "PFSC506_De_Grasse",
      "aliases": [
        "PFSC506_De_Grasse",
        "PFSC506",
        "3764303696"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC507_Toulon": {
      "name": "PFSC507_Toulon",
      "aliases": [
        "PFSC507_Toulon",
        "PFSC507",
        "3763255120"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC508_Bayard": {
      "name": "PFSC508_Bayard",
      "aliases": [
        "PFSC508_Bayard",
        "PFSC508",
        "3762206544"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC509_Carnot": {
      "name": "PFSC509_Carnot",
      "aliases": [
        "PFSC509_Carnot",
        "PFSC509",
        "3761157968"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            36
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC510_Colbert": {
      "name": "PFSC510_Colbert",
      "aliases": [
        "PFSC510_Colbert",
        "PFSC510",
        "3760109392"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16,
            20
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            21,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC516_Dupleix": {
      "name": "PFSC516_Dupleix",
      "aliases": [
        "PFSC516_Dupleix",
        "PFSC516",
        "3753817936"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC708_Metz": {
      "name": "PFSC708_Metz",
      "aliases": [
        "PFSC708_Metz",
        "PFSC708",
        "3552491344"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC710_Brennus": {
      "name": "PFSC710_Brennus",
      "aliases": [
        "PFSC710_Brennus",
        "PFSC710",
        "3550394192"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC716_Montcalm": {
      "name": "PFSC716_Montcalm",
      "aliases": [
        "PFSC716_Montcalm",
        "PFSC716",
        "3544102736"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC719_Le_Havre": {
      "name": "PFSC719_Le_Havre",
      "aliases": [
        "PFSC719_Le_Havre",
        "PFSC719",
        "3540957008"
      ],
      "mainGunCaliberMm": 330,
      "mainGunHePenMm": 55,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC730_Amiral_Lartigue": {
      "name": "PFSC730_Amiral_Lartigue",
      "aliases": [
        "PFSC730_Amiral_Lartigue",
        "PFSC730",
        "3529422672"
      ],
      "mainGunCaliberMm": 330,
      "mainGunHePenMm": 55,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            19,
            32
          ]
        },
        "side": {
          "values": [
            19,
            30,
            50,
            90
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC810_Henri_IV": {
      "name": "PFSC810_Henri_IV",
      "aliases": [
        "PFSC810_Henri_IV",
        "PFSC810",
        "3445536592"
      ],
      "mainGunCaliberMm": 240,
      "mainGunHePenMm": 40,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC819_BA_Le_Havre": {
      "name": "PFSC819_BA_Le_Havre",
      "aliases": [
        "PFSC819_BA_Le_Havre",
        "PFSC819",
        "3436099408"
      ],
      "mainGunCaliberMm": 330,
      "mainGunHePenMm": 55,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSC896_La_Galissonniere_coop": {
      "name": "PFSC896_La_Galissonniere_coop",
      "aliases": [
        "PFSC896_La_Galissonniere_coop",
        "PFSC896",
        "3355359056"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD010_Cassard": {
      "name": "PFSD010_Cassard",
      "aliases": [
        "PFSD010_Cassard",
        "PFSD010",
        "4284364624"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD015_L_Adroit": {
      "name": "PFSD015_L_Adroit",
      "aliases": [
        "PFSD015_L_Adroit",
        "PFSD015",
        "4279121744"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD016_Duchaffault": {
      "name": "PFSD016_Duchaffault",
      "aliases": [
        "PFSD016_Duchaffault",
        "PFSD016",
        "4278073168"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD017_Le_Hardi": {
      "name": "PFSD017_Le_Hardi",
      "aliases": [
        "PFSD017_Le_Hardi",
        "PFSD017",
        "4277024592"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD018_L_Aventurier": {
      "name": "PFSD018_L_Aventurier",
      "aliases": [
        "PFSD018_L_Aventurier",
        "PFSD018",
        "4275976016"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD019_Orage": {
      "name": "PFSD019_Orage",
      "aliases": [
        "PFSD019_Orage",
        "PFSD019",
        "4274927440"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD102_Enseigne_Gabolde": {
      "name": "PFSD102_Enseigne_Gabolde",
      "aliases": [
        "PFSD102_Enseigne_Gabolde",
        "PFSD102",
        "4187895632"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            9
          ],
          "stern": [
            6,
            9
          ]
        },
        "deck": {
          "values": [
            9
          ]
        },
        "side": {
          "values": [
            6,
            9
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD103_Fusilier": {
      "name": "PFSD103_Fusilier",
      "aliases": [
        "PFSD103_Fusilier",
        "PFSD103",
        "4186847056"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            9
          ],
          "stern": [
            6,
            9
          ]
        },
        "deck": {
          "values": [
            9
          ]
        },
        "side": {
          "values": [
            6,
            9
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD104_Bourrasque": {
      "name": "PFSD104_Bourrasque",
      "aliases": [
        "PFSD104_Bourrasque",
        "PFSD104",
        "4185798480"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD105_Jaguar": {
      "name": "PFSD105_Jaguar",
      "aliases": [
        "PFSD105_Jaguar",
        "PFSD105",
        "4184749904"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD106_Guepard": {
      "name": "PFSD106_Guepard",
      "aliases": [
        "PFSD106_Guepard",
        "PFSD106",
        "4183701328"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD107_Vauquelin": {
      "name": "PFSD107_Vauquelin",
      "aliases": [
        "PFSD107_Vauquelin",
        "PFSD107",
        "4182652752"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD108_Le_Fantasque": {
      "name": "PFSD108_Le_Fantasque",
      "aliases": [
        "PFSD108_Le_Fantasque",
        "PFSD108",
        "4181604176"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD109_Mogador": {
      "name": "PFSD109_Mogador",
      "aliases": [
        "PFSD109_Mogador",
        "PFSD109",
        "4180555600"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD110_Kleber": {
      "name": "PFSD110_Kleber",
      "aliases": [
        "PFSD110_Kleber",
        "PFSD110",
        "4179507024"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD210_Marceau": {
      "name": "PFSD210_Marceau",
      "aliases": [
        "PFSD210_Marceau",
        "PFSD210",
        "4074649424"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD504_Siroco": {
      "name": "PFSD504_Siroco",
      "aliases": [
        "PFSD504_Siroco",
        "PFSD504",
        "3766368080"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD506_Aigle": {
      "name": "PFSD506_Aigle",
      "aliases": [
        "PFSD506_Aigle",
        "PFSD506",
        "3764270928"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD508_Le_Terrible": {
      "name": "PFSD508_Le_Terrible",
      "aliases": [
        "PFSD508_Le_Terrible",
        "PFSD508",
        "3762173776"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD605_Cyclone_event": {
      "name": "PFSD605_Cyclone_event",
      "aliases": [
        "PFSD605_Cyclone_event",
        "PFSD605",
        "3660461904"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD710_Chateaurenault": {
      "name": "PFSD710_Chateaurenault",
      "aliases": [
        "PFSD710_Chateaurenault",
        "PFSD710",
        "3550361424"
      ],
      "mainGunCaliberMm": 105,
      "mainGunHePenMm": 26,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD718_Hoche": {
      "name": "PFSD718_Hoche",
      "aliases": [
        "PFSD718_Hoche",
        "PFSD718",
        "3541972816"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD808_TST_TERRIBLE": {
      "name": "PFSD808_TST_TERRIBLE",
      "aliases": [
        "PFSD808_TST_TERRIBLE",
        "PFSD808",
        "3447600976"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD810_Colorful_Kleber": {
      "name": "PFSD810_Colorful_Kleber",
      "aliases": [
        "PFSD810_Colorful_Kleber",
        "PFSD810",
        "3445503824"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD820_Kleber_TE": {
      "name": "PFSD820_Kleber_TE",
      "aliases": [
        "PFSD820_Kleber_TE",
        "PFSD820",
        "3435018064"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSD895_Vent": {
      "name": "PFSD895_Vent",
      "aliases": [
        "PFSD895_Vent",
        "PFSD895",
        "3356374864"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PFSS710_Surcouf": {
      "name": "PFSS710_Surcouf",
      "aliases": [
        "PFSS710_Surcouf",
        "PFSS710",
        "3549869904"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSA104_Rhein": {
      "name": "PGSA104_Rhein",
      "aliases": [
        "PGSA104_Rhein",
        "PGSA104",
        "4185896752"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16,
            25
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSA106_Weser": {
      "name": "PGSA106_Weser",
      "aliases": [
        "PGSA106_Weser",
        "PGSA106",
        "4183799600"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            30
          ],
          "stern": [
            19,
            30
          ]
        },
        "deck": {
          "values": [
            21
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PGSA108_Parseval": {
      "name": "PGSA108_Parseval",
      "aliases": [
        "PGSA108_Parseval",
        "PGSA108",
        "4181702448"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSA110_Manfred_Richthofen": {
      "name": "PGSA110_Manfred_Richthofen",
      "aliases": [
        "PGSA110_Manfred_Richthofen",
        "PGSA110",
        "4179605296"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            30,
            50
          ],
          "stern": [
            19,
            30,
            50
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            145,
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            90,
            150
          ],
          "bow": [
            60,
            150
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PGSA506_Erich_Loewenhardt": {
      "name": "PGSA506_Erich_Loewenhardt",
      "aliases": [
        "PGSA506_Erich_Loewenhardt",
        "PGSA506",
        "3764369200"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            21
          ]
        },
        "side": {
          "values": [
            20
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSA508_Graf_Zeppelin": {
      "name": "PGSA508_Graf_Zeppelin",
      "aliases": [
        "PGSA508_Graf_Zeppelin",
        "PGSA508",
        "3762272048"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            21
          ],
          "stern": [
            21
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSA510_Werner_Voss": {
      "name": "PGSA510_Werner_Voss",
      "aliases": [
        "PGSA510_Werner_Voss",
        "PGSA510",
        "3760174896"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            30,
            50
          ],
          "stern": [
            19,
            30,
            50
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            145,
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            90,
            150
          ],
          "bow": [
            60,
            150
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PGSA518_Graf_Zeppelin": {
      "name": "PGSA518_Graf_Zeppelin",
      "aliases": [
        "PGSA518_Graf_Zeppelin",
        "PGSA518",
        "3751786288"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            21
          ],
          "stern": [
            21
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSA598_Black_Graf_Zeppelin": {
      "name": "PGSA598_Black_Graf_Zeppelin",
      "aliases": [
        "PGSA598_Black_Graf_Zeppelin",
        "PGSA598",
        "3667900208"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            21
          ],
          "stern": [
            21
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSA610_Max_Immelmann": {
      "name": "PGSA610_Max_Immelmann",
      "aliases": [
        "PGSA610_Max_Immelmann",
        "PGSA610",
        "3655317296"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            30,
            50
          ],
          "stern": [
            19,
            30,
            50
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            145,
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            90,
            150
          ],
          "bow": [
            60,
            150
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PGSA910_Pinata_Richthofen": {
      "name": "PGSA910_Pinata_Richthofen",
      "aliases": [
        "PGSA910_Pinata_Richthofen",
        "PGSA910",
        "3340744496"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            30,
            50
          ],
          "stern": [
            19,
            30,
            50
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            145,
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            90,
            150
          ],
          "bow": [
            60,
            150
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PGSA990_Otto_Lilienthal": {
      "name": "PGSA990_Otto_Lilienthal",
      "aliases": [
        "PGSA990_Otto_Lilienthal",
        "PGSA990",
        "3256858416"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            30,
            50
          ],
          "stern": [
            19,
            30,
            50
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            145,
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            90,
            150
          ],
          "bow": [
            60,
            150
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PGSB002_Tirpiz_1942": {
      "name": "PGSB002_Tirpiz_1942",
      "aliases": [
        "PGSB002_Tirpiz_1942",
        "PGSB002",
        "4292818736"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            160
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60
          ],
          "bow": [
            60
          ],
          "stern": []
        }
      }
    },
    "PGSB103_Nassau": {
      "name": "PGSB103_Nassau",
      "aliases": [
        "PGSB103_Nassau",
        "PGSB103",
        "4186912560"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 71,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            160,
            210,
            240
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            80,
            90,
            100
          ],
          "bow": [
            80,
            100
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PGSB104_Kaiser": {
      "name": "PGSB104_Kaiser",
      "aliases": [
        "PGSB104_Kaiser",
        "PGSB104",
        "4185863984"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            30
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": [
            170,
            200
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            120,
            180
          ],
          "bow": [
            120,
            180
          ],
          "stern": []
        }
      }
    },
    "PGSB105_Koenig": {
      "name": "PGSB105_Koenig",
      "aliases": [
        "PGSB105_Koenig",
        "PGSB105",
        "4184815408"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19,
            20
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            170,
            200
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            150,
            200
          ],
          "bow": [
            150,
            200
          ],
          "stern": []
        }
      }
    },
    "PGSB106_Bayern": {
      "name": "PGSB106_Bayern",
      "aliases": [
        "PGSB106_Bayern",
        "PGSB106",
        "4183766832"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            170,
            250
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            30,
            150,
            200
          ],
          "bow": [
            30,
            150,
            200
          ],
          "stern": []
        }
      }
    },
    "PGSB107_Gneisenau": {
      "name": "PGSB107_Gneisenau",
      "aliases": [
        "PGSB107_Gneisenau",
        "PGSB107",
        "4182718256"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            45
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            70,
            90
          ],
          "bow": [
            70
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PGSB108_Bismarck": {
      "name": "PGSB108_Bismarck",
      "aliases": [
        "PGSB108_Bismarck",
        "PGSB108",
        "4181669680"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            160
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSB109_Friedrich_der_Grosse": {
      "name": "PGSB109_Friedrich_der_Grosse",
      "aliases": [
        "PGSB109_Friedrich_der_Grosse",
        "PGSB109",
        "4180621104"
      ],
      "mainGunCaliberMm": 420,
      "mainGunHePenMm": 105,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            50,
            80
          ]
        },
        "side": {
          "values": [
            145,
            235
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            90,
            150
          ],
          "bow": [
            60,
            150
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PGSB110_Grossdeutschland": {
      "name": "PGSB110_Grossdeutschland",
      "aliases": [
        "PGSB110_Grossdeutschland",
        "PGSB110",
        "4179572528"
      ],
      "mainGunCaliberMm": 420,
      "mainGunHePenMm": 105,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            150,
            280
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            120
          ],
          "bow": [
            60,
            120
          ],
          "stern": [
            120
          ]
        }
      }
    },
    "PGSB111_Hannover": {
      "name": "PGSB111_Hannover",
      "aliases": [
        "PGSB111_Hannover",
        "PGSB111",
        "4178523952"
      ],
      "mainGunCaliberMm": 483,
      "mainGunHePenMm": 121,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            35
          ],
          "stern": [
            32,
            35
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            180
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50,
            60,
            120,
            150
          ],
          "bow": [
            50,
            60,
            150
          ],
          "stern": [
            50,
            120,
            150
          ]
        }
      }
    },
    "PGSB203_Von_der_Tann": {
      "name": "PGSB203_Von_der_Tann",
      "aliases": [
        "PGSB203_Von_der_Tann",
        "PGSB203",
        "4082054960"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 71,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            80,
            100
          ],
          "bow": [
            80,
            100
          ],
          "stern": []
        }
      }
    },
    "PGSB204_Moltke": {
      "name": "PGSB204_Moltke",
      "aliases": [
        "PGSB204_Moltke",
        "PGSB204",
        "4081006384"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 71,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19,
            25,
            35
          ]
        },
        "side": {
          "values": [
            150,
            200
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            80,
            100,
            120
          ],
          "bow": [
            80,
            100,
            120
          ],
          "stern": [
            100
          ]
        }
      }
    },
    "PGSB205_Derfflinger": {
      "name": "PGSB205_Derfflinger",
      "aliases": [
        "PGSB205_Derfflinger",
        "PGSB205",
        "4079957808"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25,
            35
          ]
        },
        "side": {
          "values": [
            150,
            235,
            265,
            270
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            100,
            120
          ],
          "bow": [
            100,
            120
          ],
          "stern": [
            100
          ]
        }
      }
    },
    "PGSB206_Mackensen": {
      "name": "PGSB206_Mackensen",
      "aliases": [
        "PGSB206_Mackensen",
        "PGSB206",
        "4078909232"
      ],
      "mainGunCaliberMm": 350,
      "mainGunHePenMm": 88,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25,
            26
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            30,
            120
          ],
          "bow": [
            30,
            120
          ],
          "stern": []
        }
      }
    },
    "PGSB207_Prinz_Heinrich": {
      "name": "PGSB207_Prinz_Heinrich",
      "aliases": [
        "PGSB207_Prinz_Heinrich",
        "PGSB207",
        "4077860656"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            30,
            100,
            120
          ],
          "bow": [
            30,
            120
          ],
          "stern": [
            100
          ]
        }
      }
    },
    "PGSB208_Zieten": {
      "name": "PGSB208_Zieten",
      "aliases": [
        "PGSB208_Zieten",
        "PGSB208",
        "4076812080"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 102,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            170
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60
          ],
          "bow": [
            60
          ],
          "stern": []
        }
      }
    },
    "PGSB209_Prinz_Rupprecht": {
      "name": "PGSB209_Prinz_Rupprecht",
      "aliases": [
        "PGSB209_Prinz_Rupprecht",
        "PGSB209",
        "4075763504"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 102,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            20,
            27
          ],
          "stern": [
            20,
            27
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            30,
            100
          ],
          "bow": [
            30
          ],
          "stern": [
            100
          ]
        }
      }
    },
    "PGSB210_Schlieffen": {
      "name": "PGSB210_Schlieffen",
      "aliases": [
        "PGSB210_Schlieffen",
        "PGSB210",
        "4074714928"
      ],
      "mainGunCaliberMm": 420,
      "mainGunHePenMm": 105,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27,
            30
          ],
          "stern": [
            27,
            30,
            50
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            150,
            350
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            100,
            150
          ],
          "bow": [
            60,
            100
          ],
          "stern": [
            150
          ]
        }
      }
    },
    "PGSB310_Preussen": {
      "name": "PGSB310_Preussen",
      "aliases": [
        "PGSB310_Preussen",
        "PGSB310",
        "3969857328"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 114,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            150,
            280
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            120
          ],
          "bow": [
            60,
            120
          ],
          "stern": [
            120
          ]
        }
      }
    },
    "PGSB503_Koenig_Albert": {
      "name": "PGSB503_Koenig_Albert",
      "aliases": [
        "PGSB503_Koenig_Albert",
        "PGSB503",
        "3767482160"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": [
            170,
            200
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            120,
            180
          ],
          "bow": [
            120,
            180
          ],
          "stern": [
            180
          ]
        }
      }
    },
    "PGSB506_Prinz_Eithel_Friedrich": {
      "name": "PGSB506_Prinz_Eithel_Friedrich",
      "aliases": [
        "PGSB506_Prinz_Eithel_Friedrich",
        "PGSB506",
        "3764336432"
      ],
      "mainGunCaliberMm": 350,
      "mainGunHePenMm": 88,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26,
            50
          ]
        },
        "side": {
          "values": [
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSB507_Scharnhorst": {
      "name": "PGSB507_Scharnhorst",
      "aliases": [
        "PGSB507_Scharnhorst",
        "PGSB507",
        "3763287856"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 71,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            45
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            70,
            90
          ],
          "bow": [
            70
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PGSB508_Odin": {
      "name": "PGSB508_Odin",
      "aliases": [
        "PGSB508_Odin",
        "PGSB508",
        "3762239280"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            45
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            90
          ],
          "bow": [
            60
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PGSB509_Pommern": {
      "name": "PGSB509_Pommern",
      "aliases": [
        "PGSB509_Pommern",
        "PGSB509",
        "3761190704"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            50,
            80
          ]
        },
        "side": {
          "values": [
            145,
            235
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            90,
            150
          ],
          "bow": [
            60,
            150
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PGSB517_AZUR_Prinz_Heinrich": {
      "name": "PGSB517_AZUR_Prinz_Heinrich",
      "aliases": [
        "PGSB517_AZUR_Prinz_Heinrich",
        "PGSB517",
        "3752802096"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            30,
            100,
            120
          ],
          "bow": [
            30,
            120
          ],
          "stern": [
            100
          ]
        }
      }
    },
    "PGSB518_Brandenburg": {
      "name": "PGSB518_Brandenburg",
      "aliases": [
        "PGSB518_Brandenburg",
        "PGSB518",
        "3751753520"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            145
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            80
          ],
          "bow": [
            60
          ],
          "stern": [
            80
          ]
        }
      }
    },
    "PGSB528_Anhalt": {
      "name": "PGSB528_Anhalt",
      "aliases": [
        "PGSB528_Anhalt",
        "PGSB528",
        "3741267760"
      ],
      "mainGunCaliberMm": 350,
      "mainGunHePenMm": 88,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            170,
            250
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            170,
            200
          ],
          "bow": [
            170,
            200
          ],
          "stern": [
            200
          ]
        }
      }
    },
    "PGSB538_Black_Brandenburg": {
      "name": "PGSB538_Black_Brandenburg",
      "aliases": [
        "PGSB538_Black_Brandenburg",
        "PGSB538",
        "3730782000"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            145
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            80
          ],
          "bow": [
            60
          ],
          "stern": [
            80
          ]
        }
      }
    },
    "PGSB597_Black_Scharnhorst": {
      "name": "PGSB597_Black_Scharnhorst",
      "aliases": [
        "PGSB597_Black_Scharnhorst",
        "PGSB597",
        "3668916016"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 71,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            45
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            70,
            90
          ],
          "bow": [
            70
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PGSB598_Black_Tirpitz": {
      "name": "PGSB598_Black_Tirpitz",
      "aliases": [
        "PGSB598_Black_Tirpitz",
        "PGSB598",
        "3667867440"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            160
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60
          ],
          "bow": [
            60
          ],
          "stern": []
        }
      }
    },
    "PGSB599_Black_Pommern": {
      "name": "PGSB599_Black_Pommern",
      "aliases": [
        "PGSB599_Black_Pommern",
        "PGSB599",
        "3666818864"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            50,
            80
          ]
        },
        "side": {
          "values": [
            145,
            235
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            90,
            150
          ],
          "bow": [
            60,
            150
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PGSB610_Mecklenburg": {
      "name": "PGSB610_Mecklenburg",
      "aliases": [
        "PGSB610_Mecklenburg",
        "PGSB610",
        "3655284528"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            70
          ],
          "bow": [
            70
          ],
          "stern": [
            70
          ]
        }
      }
    },
    "PGSB708_Bismarck_1941": {
      "name": "PGSB708_Bismarck_1941",
      "aliases": [
        "PGSB708_Bismarck_1941",
        "PGSB708",
        "3552524080"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            160
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSB717_Scharnhorst_1943": {
      "name": "PGSB717_Scharnhorst_1943",
      "aliases": [
        "PGSB717_Scharnhorst_1943",
        "PGSB717",
        "3543086896"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 71,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            45
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            70,
            90
          ],
          "bow": [
            70
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PGSB818_BA_Tirpitz": {
      "name": "PGSB818_BA_Tirpitz",
      "aliases": [
        "PGSB818_BA_Tirpitz",
        "PGSB818",
        "3437180720"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            160
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60
          ],
          "bow": [
            60
          ],
          "stern": []
        }
      }
    },
    "PGSB828_Odin_TE": {
      "name": "PGSB828_Odin_TE",
      "aliases": [
        "PGSB828_Odin_TE",
        "PGSB828",
        "3426694960"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            90
          ],
          "bow": [
            60
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PGSB898_Azur_Bismarck": {
      "name": "PGSB898_Azur_Bismarck",
      "aliases": [
        "PGSB898_Azur_Bismarck",
        "PGSB898",
        "3353294640"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            160
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSB908_PostApoc_Zieten": {
      "name": "PGSB908_PostApoc_Zieten",
      "aliases": [
        "PGSB908_PostApoc_Zieten",
        "PGSB908",
        "3342808880"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 102,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            170
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60
          ],
          "bow": [
            60
          ],
          "stern": []
        }
      }
    },
    "PGSB910_Grossdeutschland": {
      "name": "PGSB910_Grossdeutschland",
      "aliases": [
        "PGSB910_Grossdeutschland",
        "PGSB910",
        "3340711728"
      ],
      "mainGunCaliberMm": 420,
      "mainGunHePenMm": 105,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            150,
            280
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            120
          ],
          "bow": [
            60,
            120
          ],
          "stern": [
            120
          ]
        }
      }
    },
    "PGSB918_Pirate_Brandenburg": {
      "name": "PGSB918_Pirate_Brandenburg",
      "aliases": [
        "PGSB918_Pirate_Brandenburg",
        "PGSB918",
        "3332323120"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            145
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            80
          ],
          "bow": [
            60
          ],
          "stern": [
            80
          ]
        }
      }
    },
    "PGSB920_Schlieffen": {
      "name": "PGSB920_Schlieffen",
      "aliases": [
        "PGSB920_Schlieffen",
        "PGSB920",
        "3330225968"
      ],
      "mainGunCaliberMm": 420,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27,
            30
          ],
          "stern": [
            27,
            30,
            50
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            150,
            350
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            100,
            150
          ],
          "bow": [
            60,
            100
          ],
          "stern": [
            150
          ]
        }
      }
    },
    "PGSB930_Pinata_Schliefen": {
      "name": "PGSB930_Pinata_Schliefen",
      "aliases": [
        "PGSB930_Pinata_Schliefen",
        "PGSB930",
        "3319740208"
      ],
      "mainGunCaliberMm": 420,
      "mainGunHePenMm": 105,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27,
            30
          ],
          "stern": [
            27,
            30,
            50
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            150,
            350
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            100,
            150
          ],
          "bow": [
            60,
            100
          ],
          "stern": [
            150
          ]
        }
      }
    },
    "PGSB989_Prinz_Sigismund": {
      "name": "PGSB989_Prinz_Sigismund",
      "aliases": [
        "PGSB989_Prinz_Sigismund",
        "PGSB989",
        "3257874224"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSB999_Hannover": {
      "name": "PGSB999_Hannover",
      "aliases": [
        "PGSB999_Hannover",
        "PGSB999",
        "3247388464"
      ],
      "mainGunCaliberMm": 483,
      "mainGunHePenMm": 121,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            35
          ],
          "stern": [
            32,
            35
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            180
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50,
            60,
            120,
            150
          ],
          "bow": [
            50,
            60,
            150
          ],
          "stern": [
            50,
            120,
            150
          ]
        }
      }
    },
    "PGSC001_Hermelin_1940": {
      "name": "PGSC001_Hermelin_1940",
      "aliases": [
        "PGSC001_Hermelin_1940",
        "PGSC001",
        "4293834544"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": [
            23,
            35
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC002_Drezden_1908": {
      "name": "PGSC002_Drezden_1908",
      "aliases": [
        "PGSC002_Drezden_1908",
        "PGSC002",
        "4292785968"
      ],
      "mainGunCaliberMm": 105,
      "mainGunHePenMm": 26,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6,
            9
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC010_Prinz_Adalbert": {
      "name": "PGSC010_Prinz_Adalbert",
      "aliases": [
        "PGSC010_Prinz_Adalbert",
        "PGSC010",
        "4284397360"
      ],
      "mainGunCaliberMm": 350,
      "mainGunHePenMm": 88,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            100,
            200
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC016_Deutschland": {
      "name": "PGSC016_Deutschland",
      "aliases": [
        "PGSC016_Deutschland",
        "PGSC016",
        "4278105904"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 71,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25,
            100
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            100
          ],
          "bow": [
            100
          ],
          "stern": []
        }
      }
    },
    "PGSC017_Admiral_Scheer": {
      "name": "PGSC017_Admiral_Scheer",
      "aliases": [
        "PGSC017_Admiral_Scheer",
        "PGSC017",
        "4277057328"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 71,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC018_Knesebeck": {
      "name": "PGSC018_Knesebeck",
      "aliases": [
        "PGSC018_Knesebeck",
        "PGSC018",
        "4276008752"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC019_Manteuffel": {
      "name": "PGSC019_Manteuffel",
      "aliases": [
        "PGSC019_Manteuffel",
        "PGSC019",
        "4274960176"
      ],
      "mainGunCaliberMm": 350,
      "mainGunHePenMm": 88,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            90
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC103_Kolberg": {
      "name": "PGSC103_Kolberg",
      "aliases": [
        "PGSC103_Kolberg",
        "PGSC103",
        "4186879792"
      ],
      "mainGunCaliberMm": 105,
      "mainGunHePenMm": 26,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC104_Karlsruhe": {
      "name": "PGSC104_Karlsruhe",
      "aliases": [
        "PGSC104_Karlsruhe",
        "PGSC104",
        "4185831216"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16,
            60
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            30,
            60
          ],
          "bow": [
            30,
            60
          ],
          "stern": []
        }
      }
    },
    "PGSC105_Konigsberg": {
      "name": "PGSC105_Konigsberg",
      "aliases": [
        "PGSC105_Konigsberg",
        "PGSC105",
        "4184782640"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            20,
            35
          ],
          "bow": [
            20
          ],
          "stern": [
            35
          ]
        }
      }
    },
    "PGSC106_Nurnberg": {
      "name": "PGSC106_Nurnberg",
      "aliases": [
        "PGSC106_Nurnberg",
        "PGSC106",
        "4183734064"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            20
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC107_Yorck": {
      "name": "PGSC107_Yorck",
      "aliases": [
        "PGSC107_Yorck",
        "PGSC107",
        "4182685488"
      ],
      "mainGunCaliberMm": 210,
      "mainGunHePenMm": 53,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC108_Hipper": {
      "name": "PGSC108_Hipper",
      "aliases": [
        "PGSC108_Hipper",
        "PGSC108",
        "4181636912"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PGSC109_Roon": {
      "name": "PGSC109_Roon",
      "aliases": [
        "PGSC109_Roon",
        "PGSC109",
        "4180588336"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PGSC110_Hindenburg": {
      "name": "PGSC110_Hindenburg",
      "aliases": [
        "PGSC110_Hindenburg",
        "PGSC110",
        "4179539760"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PGSC111_Clausewitz": {
      "name": "PGSC111_Clausewitz",
      "aliases": [
        "PGSC111_Clausewitz",
        "PGSC111",
        "4178491184"
      ],
      "mainGunCaliberMm": 210,
      "mainGunHePenMm": 53,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC502_Emden_1908": {
      "name": "PGSC502_Emden_1908",
      "aliases": [
        "PGSC502_Emden_1908",
        "PGSC502",
        "3768497968"
      ],
      "mainGunCaliberMm": 105,
      "mainGunHePenMm": 26,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6,
            9
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC506_Admiral_Graf_Spee": {
      "name": "PGSC506_Admiral_Graf_Spee",
      "aliases": [
        "PGSC506_Admiral_Graf_Spee",
        "PGSC506",
        "3764303664"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 71,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC507_Munchen": {
      "name": "PGSC507_Munchen",
      "aliases": [
        "PGSC507_Munchen",
        "PGSC507",
        "3763255088"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            20
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC508_Prinz_Eugen": {
      "name": "PGSC508_Prinz_Eugen",
      "aliases": [
        "PGSC508_Prinz_Eugen",
        "PGSC508",
        "3762206512"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PGSC509_Siegfried": {
      "name": "PGSC509_Siegfried",
      "aliases": [
        "PGSC509_Siegfried",
        "PGSC509",
        "3761157936"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            90
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC516_Leipzig": {
      "name": "PGSC516_Leipzig",
      "aliases": [
        "PGSC516_Leipzig",
        "PGSC516",
        "3753817904"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16,
            40,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            20
          ],
          "bow": [
            20
          ],
          "stern": [
            20
          ]
        }
      }
    },
    "PGSC517_Weimar": {
      "name": "PGSC517_Weimar",
      "aliases": [
        "PGSC517_Weimar",
        "PGSC517",
        "3752769328"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC518_Mainz": {
      "name": "PGSC518_Mainz",
      "aliases": [
        "PGSC518_Mainz",
        "PGSC518",
        "3751720752"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40,
            70
          ],
          "bow": [
            40
          ],
          "stern": [
            70
          ]
        }
      }
    },
    "PGSC519_Aegir": {
      "name": "PGSC519_Aegir",
      "aliases": [
        "PGSC519_Aegir",
        "PGSC519",
        "3750672176"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            90
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC528_Schill": {
      "name": "PGSC528_Schill",
      "aliases": [
        "PGSC528_Schill",
        "PGSC528",
        "3741234992"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 71,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            30
          ],
          "bow": [
            30
          ],
          "stern": []
        }
      }
    },
    "PGSC529_Admiral_Schroder": {
      "name": "PGSC529_Admiral_Schroder",
      "aliases": [
        "PGSC529_Admiral_Schroder",
        "PGSC529",
        "3740186416"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            90
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC598_Black_Mainz": {
      "name": "PGSC598_Black_Mainz",
      "aliases": [
        "PGSC598_Black_Mainz",
        "PGSC598",
        "3667834672"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40,
            70
          ],
          "bow": [
            40
          ],
          "stern": [
            70
          ]
        }
      }
    },
    "PGSC706_HSF_Graf_Spee": {
      "name": "PGSC706_HSF_Graf_Spee",
      "aliases": [
        "PGSC706_HSF_Graf_Spee",
        "PGSC706",
        "3554588464"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 71,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC710_Hildebrand": {
      "name": "PGSC710_Hildebrand",
      "aliases": [
        "PGSC710_Hildebrand",
        "PGSC710",
        "3550394160"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            19,
            30
          ]
        },
        "side": {
          "values": [
            19,
            50,
            90
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC717_Nurnberg_1944": {
      "name": "PGSC717_Nurnberg_1944",
      "aliases": [
        "PGSC717_Nurnberg_1944",
        "PGSC717",
        "3543054128"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            20
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC718_Warhammer_Blacktemplar": {
      "name": "PGSC718_Warhammer_Blacktemplar",
      "aliases": [
        "PGSC718_Warhammer_Blacktemplar",
        "PGSC718",
        "3542005552"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40,
            70
          ],
          "bow": [
            40
          ],
          "stern": [
            70
          ]
        }
      }
    },
    "PGSC720_Bremen": {
      "name": "PGSC720_Bremen",
      "aliases": [
        "PGSC720_Bremen",
        "PGSC720",
        "3539908400"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC728_Wiesbaden": {
      "name": "PGSC728_Wiesbaden",
      "aliases": [
        "PGSC728_Wiesbaden",
        "PGSC728",
        "3531519792"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC729_Blucher": {
      "name": "PGSC729_Blucher",
      "aliases": [
        "PGSC729_Blucher",
        "PGSC729",
        "3530471216"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PGSC809_Colorful_Roon": {
      "name": "PGSC809_Colorful_Roon",
      "aliases": [
        "PGSC809_Colorful_Roon",
        "PGSC809",
        "3446585136"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PGSC817_Black_Munchen": {
      "name": "PGSC817_Black_Munchen",
      "aliases": [
        "PGSC817_Black_Munchen",
        "PGSC817",
        "3438196528"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            20
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC890_Azur_Hindenburg": {
      "name": "PGSC890_Azur_Hindenburg",
      "aliases": [
        "PGSC890_Azur_Hindenburg",
        "PGSC890",
        "3361650480"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PGSC891_Clausewitz_PLUS": {
      "name": "PGSC891_Clausewitz_PLUS",
      "aliases": [
        "PGSC891_Clausewitz_PLUS",
        "PGSC891",
        "3360601904"
      ],
      "mainGunCaliberMm": 210,
      "mainGunHePenMm": 53,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC899_AZUR_Aegir": {
      "name": "PGSC899_AZUR_Aegir",
      "aliases": [
        "PGSC899_AZUR_Aegir",
        "PGSC899",
        "3352213296"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            90
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC908_Black_Schill": {
      "name": "PGSC908_Black_Schill",
      "aliases": [
        "PGSC908_Black_Schill",
        "PGSC908",
        "3342776112"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 71,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            30
          ],
          "bow": [
            30
          ],
          "stern": []
        }
      }
    },
    "PGSC910_Hindenburg": {
      "name": "PGSC910_Hindenburg",
      "aliases": [
        "PGSC910_Hindenburg",
        "PGSC910",
        "3340678960"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PGSC920_Gold_Bremen": {
      "name": "PGSC920_Gold_Bremen",
      "aliases": [
        "PGSC920_Gold_Bremen",
        "PGSC920",
        "3330193200"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSC996_Admiral_Reinhard": {
      "name": "PGSC996_Admiral_Reinhard",
      "aliases": [
        "PGSC996_Admiral_Reinhard",
        "PGSC996",
        "3250501424"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 71,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD102_V_25": {
      "name": "PGSD102_V_25",
      "aliases": [
        "PGSD102_V_25",
        "PGSD102",
        "4187895600"
      ],
      "mainGunCaliberMm": 105,
      "mainGunHePenMm": 26,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            9
          ],
          "stern": [
            6,
            9
          ]
        },
        "deck": {
          "values": [
            9
          ]
        },
        "side": {
          "values": [
            6,
            9
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD103_G_101": {
      "name": "PGSD103_G_101",
      "aliases": [
        "PGSD103_G_101",
        "PGSD103",
        "4186847024"
      ],
      "mainGunCaliberMm": 105,
      "mainGunHePenMm": 26,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD104_V_170": {
      "name": "PGSD104_V_170",
      "aliases": [
        "PGSD104_V_170",
        "PGSD104",
        "4185798448"
      ],
      "mainGunCaliberMm": 105,
      "mainGunHePenMm": 26,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            13
          ],
          "stern": [
            10,
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD105_T_22": {
      "name": "PGSD105_T_22",
      "aliases": [
        "PGSD105_T_22",
        "PGSD105",
        "4184749872"
      ],
      "mainGunCaliberMm": 105,
      "mainGunHePenMm": 26,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            16
          ],
          "stern": [
            10,
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD106_Ernst_Gaede": {
      "name": "PGSD106_Ernst_Gaede",
      "aliases": [
        "PGSD106_Ernst_Gaede",
        "PGSD106",
        "4183701296"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD107_Leberecht_Maass": {
      "name": "PGSD107_Leberecht_Maass",
      "aliases": [
        "PGSD107_Leberecht_Maass",
        "PGSD107",
        "4182652720"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD108_Z_23": {
      "name": "PGSD108_Z_23",
      "aliases": [
        "PGSD108_Z_23",
        "PGSD108",
        "4181604144"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD109_Z_46": {
      "name": "PGSD109_Z_46",
      "aliases": [
        "PGSD109_Z_46",
        "PGSD109",
        "4180555568"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD110_Z_52": {
      "name": "PGSD110_Z_52",
      "aliases": [
        "PGSD110_Z_52",
        "PGSD110",
        "4179506992"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD111_Z_57": {
      "name": "PGSD111_Z_57",
      "aliases": [
        "PGSD111_Z_57",
        "PGSD111",
        "4178458416"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD207_Z_31": {
      "name": "PGSD207_Z_31",
      "aliases": [
        "PGSD207_Z_31",
        "PGSD207",
        "4077795120"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            25
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD208_Gustav_Julius_Maerker": {
      "name": "PGSD208_Gustav_Julius_Maerker",
      "aliases": [
        "PGSD208_Gustav_Julius_Maerker",
        "PGSD208",
        "4076746544"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD209_Felix_Schultz": {
      "name": "PGSD209_Felix_Schultz",
      "aliases": [
        "PGSD209_Felix_Schultz",
        "PGSD209",
        "4075697968"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD210_Elbing": {
      "name": "PGSD210_Elbing",
      "aliases": [
        "PGSD210_Elbing",
        "PGSD210",
        "4074649392"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD506_T_61": {
      "name": "PGSD506_T_61",
      "aliases": [
        "PGSD506_T_61",
        "PGSD506",
        "3764270896"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD508_Z_39": {
      "name": "PGSD508_Z_39",
      "aliases": [
        "PGSD508_Z_39",
        "PGSD508",
        "3762173744"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD516_Karl_von_Schonberg": {
      "name": "PGSD516_Karl_von_Schonberg",
      "aliases": [
        "PGSD516_Karl_von_Schonberg",
        "PGSD516",
        "3753785136"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD518_Z_35": {
      "name": "PGSD518_Z_35",
      "aliases": [
        "PGSD518_Z_35",
        "PGSD518",
        "3751687984"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD519_Z_44": {
      "name": "PGSD519_Z_44",
      "aliases": [
        "PGSD519_Z_44",
        "PGSD519",
        "3750639408"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD529_ZF_6": {
      "name": "PGSD529_ZF_6",
      "aliases": [
        "PGSD529_ZF_6",
        "PGSD529",
        "3740153648"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD610_Z_42": {
      "name": "PGSD610_Z_42",
      "aliases": [
        "PGSD610_Z_42",
        "PGSD610",
        "3655218992"
      ],
      "mainGunCaliberMm": 105,
      "mainGunHePenMm": 26,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD707_Z32_EventDday_Torp": {
      "name": "PGSD707_Z32_EventDday_Torp",
      "aliases": [
        "PGSD707_Z32_EventDday_Torp",
        "PGSD707",
        "3553507120"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD709_GM_ZF_6": {
      "name": "PGSD709_GM_ZF_6",
      "aliases": [
        "PGSD709_GM_ZF_6",
        "PGSD709",
        "3551409968"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD710_Georg_Hoffmann": {
      "name": "PGSD710_Georg_Hoffmann",
      "aliases": [
        "PGSD710_Georg_Hoffmann",
        "PGSD710",
        "3550361392"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            25
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD717_Z33_EventDday_MG": {
      "name": "PGSD717_Z33_EventDday_MG",
      "aliases": [
        "PGSD717_Z33_EventDday_MG",
        "PGSD717",
        "3543021360"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD719_ZH_1": {
      "name": "PGSD719_ZH_1",
      "aliases": [
        "PGSD719_ZH_1",
        "PGSD719",
        "3540924208"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD720_Gold_Georg_Hoffmann": {
      "name": "PGSD720_Gold_Georg_Hoffmann",
      "aliases": [
        "PGSD720_Gold_Georg_Hoffmann",
        "PGSD720",
        "3539875632"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            25
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD727_z34_EventDday_Support": {
      "name": "PGSD727_z34_EventDday_Support",
      "aliases": [
        "PGSD727_z34_EventDday_Support",
        "PGSD727",
        "3532535600"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD737_z38_EventDday_Heal": {
      "name": "PGSD737_z38_EventDday_Heal",
      "aliases": [
        "PGSD737_z38_EventDday_Heal",
        "PGSD737",
        "3522049840"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD910_East_Z_52": {
      "name": "PGSD910_East_Z_52",
      "aliases": [
        "PGSD910_East_Z_52",
        "PGSD910",
        "3340646192"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSD990_Lubeck": {
      "name": "PGSD990_Lubeck",
      "aliases": [
        "PGSD990_Lubeck",
        "PGSD990",
        "3256760112"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSS106_U_69": {
      "name": "PGSS106_U_69",
      "aliases": [
        "PGSS106_U_69",
        "PGSS106",
        "4183209776"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            13,
            16,
            19
          ],
          "stern": [
            6,
            13,
            16,
            19
          ]
        },
        "deck": {
          "values": [
            6,
            13,
            16,
            19
          ]
        },
        "side": {
          "values": [
            6,
            13,
            16,
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSS108_U190": {
      "name": "PGSS108_U190",
      "aliases": [
        "PGSS108_U190",
        "PGSS108",
        "4181112624"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            16,
            19,
            25
          ],
          "stern": [
            6,
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSS110_U_2501": {
      "name": "PGSS110_U_2501",
      "aliases": [
        "PGSS110_U_2501",
        "PGSS110",
        "4179015472"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            16,
            19,
            25
          ],
          "stern": [
            6,
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSS206_U_69": {
      "name": "PGSS206_U_69",
      "aliases": [
        "PGSS206_U_69",
        "PGSS206",
        "4078352176"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            13,
            16,
            19
          ],
          "stern": [
            6,
            13,
            16,
            19
          ]
        },
        "deck": {
          "values": [
            6,
            13,
            16,
            19
          ]
        },
        "side": {
          "values": [
            6,
            13,
            16,
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSS208_U190": {
      "name": "PGSS208_U190",
      "aliases": [
        "PGSS208_U190",
        "PGSS208",
        "4076255024"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            16,
            19,
            25
          ],
          "stern": [
            6,
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSS210_U_2501": {
      "name": "PGSS210_U_2501",
      "aliases": [
        "PGSS210_U_2501",
        "PGSS210",
        "4074157872"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            16,
            19,
            25
          ],
          "stern": [
            6,
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            6,
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PGSS510_U4501": {
      "name": "PGSS510_U4501",
      "aliases": [
        "PGSS510_U4501",
        "PGSS510",
        "3759585072"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSB710_Willem_de_Eerste": {
      "name": "PHSB710_Willem_de_Eerste",
      "aliases": [
        "PHSB710_Willem_de_Eerste",
        "PHSB710",
        "3550426896"
      ],
      "mainGunCaliberMm": 419,
      "mainGunHePenMm": 70,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSC010_Utrecht": {
      "name": "PHSC010_Utrecht",
      "aliases": [
        "PHSC010_Utrecht",
        "PHSC010",
        "4284397328"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSC018_Jaarsveld": {
      "name": "PHSC018_Jaarsveld",
      "aliases": [
        "PHSC018_Jaarsveld",
        "PHSC018",
        "4276008720"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSC019_Menno_Van_Coehoorn": {
      "name": "PHSC019_Menno_Van_Coehoorn",
      "aliases": [
        "PHSC019_Menno_Van_Coehoorn",
        "PHSC019",
        "4274960144"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSC101_Van_Kinsbergen": {
      "name": "PHSC101_Van_Kinsbergen",
      "aliases": [
        "PHSC101_Van_Kinsbergen",
        "PHSC101",
        "4188976912"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            20
          ],
          "stern": [
            20
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSC102_Gelderland": {
      "name": "PHSC102_Gelderland",
      "aliases": [
        "PHSC102_Gelderland",
        "PHSC102",
        "4187928336"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSC103_Java": {
      "name": "PHSC103_Java",
      "aliases": [
        "PHSC103_Java",
        "PHSC103",
        "4186879760"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSC104_De_Ruyter": {
      "name": "PHSC104_De_Ruyter",
      "aliases": [
        "PHSC104_De_Ruyter",
        "PHSC104",
        "4185831184"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSC105_Celebes": {
      "name": "PHSC105_Celebes",
      "aliases": [
        "PHSC105_Celebes",
        "PHSC105",
        "4184782608"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSC106_Kijkduin": {
      "name": "PHSC106_Kijkduin",
      "aliases": [
        "PHSC106_Kijkduin",
        "PHSC106",
        "4183734032"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16,
            20
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16,
            20,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSC107_Eendracht": {
      "name": "PHSC107_Eendracht",
      "aliases": [
        "PHSC107_Eendracht",
        "PHSC107",
        "4182685456"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            20
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16,
            20,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSC108_Haarlem": {
      "name": "PHSC108_Haarlem",
      "aliases": [
        "PHSC108_Haarlem",
        "PHSC108",
        "4181636880"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40,
            50
          ],
          "bow": [
            40
          ],
          "stern": [
            50
          ]
        }
      }
    },
    "PHSC109_Johan_de_Witt": {
      "name": "PHSC109_Johan_de_Witt",
      "aliases": [
        "PHSC109_Johan_de_Witt",
        "PHSC109",
        "4180588304"
      ],
      "mainGunCaliberMm": 240,
      "mainGunHePenMm": 40,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PHSC110_Gouden_Leeuw": {
      "name": "PHSC110_Gouden_Leeuw",
      "aliases": [
        "PHSC110_Gouden_Leeuw",
        "PHSC110",
        "4179539728"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 47,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PHSC508_De_Zeven_Provincien": {
      "name": "PHSC508_De_Zeven_Provincien",
      "aliases": [
        "PHSC508_De_Zeven_Provincien",
        "PHSC508",
        "3762206480"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSC509_Van_Speijk": {
      "name": "PHSC509_Van_Speijk",
      "aliases": [
        "PHSC509_Van_Speijk",
        "PHSC509",
        "3761157904"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50
          ],
          "bow": [
            50
          ],
          "stern": [
            50
          ]
        }
      }
    },
    "PHSC708_Vrijheid": {
      "name": "PHSC708_Vrijheid",
      "aliases": [
        "PHSC708_Vrijheid",
        "PHSC708",
        "3552491280"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSC710_Prins_Van_Oranje": {
      "name": "PHSC710_Prins_Van_Oranje",
      "aliases": [
        "PHSC710_Prins_Van_Oranje",
        "PHSC710",
        "3550394128"
      ],
      "mainGunCaliberMm": 234,
      "mainGunHePenMm": 39,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PHSC720_Gold_Prins_Van_Oranje": {
      "name": "PHSC720_Gold_Prins_Van_Oranje",
      "aliases": [
        "PHSC720_Gold_Prins_Van_Oranje",
        "PHSC720",
        "3539908368"
      ],
      "mainGunCaliberMm": 234,
      "mainGunHePenMm": 39,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PHSC730_Unie": {
      "name": "PHSC730_Unie",
      "aliases": [
        "PHSC730_Unie",
        "PHSC730",
        "3529422608"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSC988_Admiraal": {
      "name": "PHSC988_Admiraal",
      "aliases": [
        "PHSC988_Admiraal",
        "PHSC988",
        "3258890000"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSC990_Vrijheid": {
      "name": "PHSC990_Vrijheid",
      "aliases": [
        "PHSC990_Vrijheid",
        "PHSC990",
        "3256792848"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 47,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PHSC998_Statenland": {
      "name": "PHSC998_Statenland",
      "aliases": [
        "PHSC998_Statenland",
        "PHSC998",
        "3248404240"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSD509_Groningen": {
      "name": "PHSD509_Groningen",
      "aliases": [
        "PHSD509_Groningen",
        "PHSD509",
        "3761125136"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSD610_Tromp": {
      "name": "PHSD610_Tromp",
      "aliases": [
        "PHSD610_Tromp",
        "PHSD610",
        "3655218960"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PHSS710_Tonijn": {
      "name": "PHSS710_Tonijn",
      "aliases": [
        "PHSS710_Tonijn",
        "PHSS710",
        "3549869840"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISA508_Aquila": {
      "name": "PISA508_Aquila",
      "aliases": [
        "PISA508_Aquila",
        "PISA508",
        "3762271984"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISB011_Affondatore": {
      "name": "PISB011_Affondatore",
      "aliases": [
        "PISB011_Affondatore",
        "PISB011",
        "4283381488"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 102.4,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            50,
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISB104_Dante_Alighieri": {
      "name": "PISB104_Dante_Alighieri",
      "aliases": [
        "PISB104_Dante_Alighieri",
        "PISB104",
        "4185863920"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 79.2,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            100
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            76,
            100
          ],
          "bow": [
            100
          ],
          "stern": [
            76
          ]
        }
      }
    },
    "PISB105_Conte_di_Cavour": {
      "name": "PISB105_Conte_di_Cavour",
      "aliases": [
        "PISB105_Conte_di_Cavour",
        "PISB105",
        "4184815344"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 79.2,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            22,
            30
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            43
          ]
        },
        "side": {
          "values": [
            130
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            85,
            110,
            130
          ],
          "bow": [
            85,
            110,
            130
          ],
          "stern": [
            85,
            110,
            130
          ]
        }
      }
    },
    "PISB106_Andrea_Doria": {
      "name": "PISB106_Andrea_Doria",
      "aliases": [
        "PISB106_Andrea_Doria",
        "PISB106",
        "4183766768"
      ],
      "mainGunCaliberMm": 320,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 82.7,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            38,
            44
          ]
        },
        "side": {
          "values": [
            70,
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISB107_Francesco_Caracciolo": {
      "name": "PISB107_Francesco_Caracciolo",
      "aliases": [
        "PISB107_Francesco_Caracciolo",
        "PISB107",
        "4182718192"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 96.7,
      "armor": {
        "bowStern": {
          "bow": [
            26,
            80
          ],
          "stern": [
            26,
            80
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            150,
            220
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            150,
            300
          ],
          "bow": [
            150,
            300
          ],
          "stern": [
            300
          ]
        }
      }
    },
    "PISB108_Vittorio_Veneto": {
      "name": "PISB108_Vittorio_Veneto",
      "aliases": [
        "PISB108_Vittorio_Veneto",
        "PISB108",
        "4181669616"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 96.7,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            70
          ],
          "stern": [
            13,
            32
          ]
        },
        "deck": {
          "values": [
            45
          ]
        },
        "side": {
          "values": [
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            130
          ],
          "bow": [
            130
          ],
          "stern": []
        }
      }
    },
    "PISB109_Lepanto": {
      "name": "PISB109_Lepanto",
      "aliases": [
        "PISB109_Lepanto",
        "PISB109",
        "4180621040"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 96.7,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            55
          ]
        },
        "side": {
          "values": [
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            80
          ],
          "bow": [
            60,
            80
          ],
          "stern": []
        }
      }
    },
    "PISB110_Cristoforo_Colombo": {
      "name": "PISB110_Cristoforo_Colombo",
      "aliases": [
        "PISB110_Cristoforo_Colombo",
        "PISB110",
        "4179572464"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 96.7,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60
          ],
          "bow": [
            60
          ],
          "stern": [
            60
          ]
        }
      }
    },
    "PISB505_Giulio_Cesare": {
      "name": "PISB505_Giulio_Cesare",
      "aliases": [
        "PISB505_Giulio_Cesare",
        "PISB505",
        "3765384944"
      ],
      "mainGunCaliberMm": 320,
      "mainGunHePenMm": 55,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19,
            43
          ]
        },
        "side": {
          "values": [
            130
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            110
          ],
          "bow": [
            110
          ],
          "stern": []
        }
      }
    },
    "PISB508_Roma": {
      "name": "PISB508_Roma",
      "aliases": [
        "PISB508_Roma",
        "PISB508",
        "3762239216"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            45
          ]
        },
        "side": {
          "values": [
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            130
          ],
          "bow": [
            130
          ],
          "stern": []
        }
      }
    },
    "PISB509_Marco_Polo": {
      "name": "PISB509_Marco_Polo",
      "aliases": [
        "PISB509_Marco_Polo",
        "PISB509",
        "3761190640"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 102.4,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            55
          ]
        },
        "side": {
          "values": [
            60,
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            130
          ],
          "bow": [
            130
          ],
          "stern": []
        }
      }
    },
    "PISB510_Ruggiero_di_Lauria": {
      "name": "PISB510_Ruggiero_di_Lauria",
      "aliases": [
        "PISB510_Ruggiero_di_Lauria",
        "PISB510",
        "3760142064"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 114,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            120
          ]
        },
        "side": {
          "values": [
            32,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISB519_Giuseppe_Verdi": {
      "name": "PISB519_Giuseppe_Verdi",
      "aliases": [
        "PISB519_Giuseppe_Verdi",
        "PISB519",
        "3750704880"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            55
          ]
        },
        "side": {
          "values": [
            60,
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            130
          ],
          "bow": [
            130
          ],
          "stern": []
        }
      }
    },
    "PISB708_AZUR_Littorio": {
      "name": "PISB708_AZUR_Littorio",
      "aliases": [
        "PISB708_AZUR_Littorio",
        "PISB708",
        "3552524016"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            45
          ]
        },
        "side": {
          "values": [
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            130
          ],
          "bow": [
            130
          ],
          "stern": []
        }
      }
    },
    "PISB709_Olympian_Marco_Polo": {
      "name": "PISB709_Olympian_Marco_Polo",
      "aliases": [
        "PISB709_Olympian_Marco_Polo",
        "PISB709",
        "3551475440"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 102.4,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            55
          ]
        },
        "side": {
          "values": [
            60,
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            130
          ],
          "bow": [
            130
          ],
          "stern": []
        }
      }
    },
    "PISB710_Sicilia": {
      "name": "PISB710_Sicilia",
      "aliases": [
        "PISB710_Sicilia",
        "PISB710",
        "3550426864"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60
          ],
          "bow": [
            60
          ],
          "stern": [
            60
          ]
        }
      }
    },
    "PISB718_Marcantonio_Colonna": {
      "name": "PISB718_Marcantonio_Colonna",
      "aliases": [
        "PISB718_Marcantonio_Colonna",
        "PISB718",
        "3542038256"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25,
            80
          ],
          "stern": [
            25,
            80
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            150,
            220
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            300
          ],
          "bow": [
            300
          ],
          "stern": [
            300
          ]
        }
      }
    },
    "PISB719_Olympian_Giuseppe_Verdi": {
      "name": "PISB719_Olympian_Giuseppe_Verdi",
      "aliases": [
        "PISB719_Olympian_Giuseppe_Verdi",
        "PISB719",
        "3540989680"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            55
          ]
        },
        "side": {
          "values": [
            60,
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            130
          ],
          "bow": [
            130
          ],
          "stern": []
        }
      }
    },
    "PISB805_TST_CESARE": {
      "name": "PISB805_TST_CESARE",
      "aliases": [
        "PISB805_TST_CESARE",
        "PISB805",
        "3450812144"
      ],
      "mainGunCaliberMm": 320,
      "mainGunHePenMm": 55,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            25,
            43
          ]
        },
        "side": {
          "values": [
            130
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            110
          ],
          "bow": [
            110
          ],
          "stern": []
        }
      }
    },
    "PISB810_Cyber_Ruggiero_di_Lauria": {
      "name": "PISB810_Cyber_Ruggiero_di_Lauria",
      "aliases": [
        "PISB810_Cyber_Ruggiero_di_Lauria",
        "PISB810",
        "3445569264"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 114,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            120
          ]
        },
        "side": {
          "values": [
            32,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISB818_BA_Marcantonio_Colonna": {
      "name": "PISB818_BA_Marcantonio_Colonna",
      "aliases": [
        "PISB818_BA_Marcantonio_Colonna",
        "PISB818",
        "3437180656"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25,
            80
          ],
          "stern": [
            25,
            80
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            150,
            220
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            300
          ],
          "bow": [
            300
          ],
          "stern": [
            300
          ]
        }
      }
    },
    "PISB908_FBO_Roma": {
      "name": "PISB908_FBO_Roma",
      "aliases": [
        "PISB908_FBO_Roma",
        "PISB908",
        "3342808816"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            45
          ]
        },
        "side": {
          "values": [
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            130
          ],
          "bow": [
            130
          ],
          "stern": []
        }
      }
    },
    "PISB909_Azur_Marco_Polo": {
      "name": "PISB909_Azur_Marco_Polo",
      "aliases": [
        "PISB909_Azur_Marco_Polo",
        "PISB909",
        "3341760240"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 102.4,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            55
          ]
        },
        "side": {
          "values": [
            60,
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            130
          ],
          "bow": [
            130
          ],
          "stern": []
        }
      }
    },
    "PISB990_Amerigo_Vespucci": {
      "name": "PISB990_Amerigo_Vespucci",
      "aliases": [
        "PISB990_Amerigo_Vespucci",
        "PISB990",
        "3256825584"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 96.7,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60
          ],
          "bow": [
            60
          ],
          "stern": [
            60
          ]
        }
      }
    },
    "PISC101_Eritrea": {
      "name": "PISC101_Eritrea",
      "aliases": [
        "PISC101_Eritrea",
        "PISC101",
        "4188976880"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC102_Nino_Bixio": {
      "name": "PISC102_Nino_Bixio",
      "aliases": [
        "PISC102_Nino_Bixio",
        "PISC102",
        "4187928304"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 34.2,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC103_Taranto": {
      "name": "PISC103_Taranto",
      "aliases": [
        "PISC103_Taranto",
        "PISC103",
        "4186879728"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 41.8,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60
          ],
          "bow": [
            60
          ],
          "stern": []
        }
      }
    },
    "PISC104_Alberto_da_Giussano": {
      "name": "PISC104_Alberto_da_Giussano",
      "aliases": [
        "PISC104_Alberto_da_Giussano",
        "PISC104",
        "4185831152"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 42.3,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            16,
            24
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC105_Raimondo_Montecuccoli": {
      "name": "PISC105_Raimondo_Montecuccoli",
      "aliases": [
        "PISC105_Raimondo_Montecuccoli",
        "PISC105",
        "4184782576"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 42.3,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            20,
            60
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC106_Trento": {
      "name": "PISC106_Trento",
      "aliases": [
        "PISC106_Trento",
        "PISC106",
        "4183734000"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 54.9,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC107_Zara": {
      "name": "PISC107_Zara",
      "aliases": [
        "PISC107_Zara",
        "PISC107",
        "4182685424"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 54.9,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC108_Amalfi": {
      "name": "PISC108_Amalfi",
      "aliases": [
        "PISC108_Amalfi",
        "PISC108",
        "4181636848"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 54.9,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC109_Brindisi": {
      "name": "PISC109_Brindisi",
      "aliases": [
        "PISC109_Brindisi",
        "PISC109",
        "4180588272"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 54.9,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC110_Venezia": {
      "name": "PISC110_Venezia",
      "aliases": [
        "PISC110_Venezia",
        "PISC110",
        "4179539696"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 54.9,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30,
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40,
            60
          ],
          "bow": [
            40
          ],
          "stern": [
            40,
            60
          ]
        }
      }
    },
    "PISC111_Piemonte": {
      "name": "PISC111_Piemonte",
      "aliases": [
        "PISC111_Piemonte",
        "PISC111",
        "4178491120"
      ],
      "mainGunCaliberMm": 254,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 67.2,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PISC505_Genova": {
      "name": "PISC505_Genova",
      "aliases": [
        "PISC505_Genova",
        "PISC505",
        "3765352176"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 54.9,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC506_DucadAosta": {
      "name": "PISC506_DucadAosta",
      "aliases": [
        "PISC506_DucadAosta",
        "PISC506",
        "3764303600"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            30
          ],
          "stern": [
            16,
            30
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            20,
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC507_Duca_degli_Abruzzi": {
      "name": "PISC507_Duca_degli_Abruzzi",
      "aliases": [
        "PISC507_Duca_degli_Abruzzi",
        "PISC507",
        "3763255024"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            20,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            30
          ],
          "bow": [
            30
          ],
          "stern": []
        }
      }
    },
    "PISC510_Napoli": {
      "name": "PISC510_Napoli",
      "aliases": [
        "PISC510_Napoli",
        "PISC510",
        "3760109296"
      ],
      "mainGunCaliberMm": 254,
      "mainGunHePenMm": 42,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            60
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60
          ],
          "bow": [
            60
          ],
          "stern": [
            60
          ]
        }
      }
    },
    "PISC517_Francesco_Ferruccio": {
      "name": "PISC517_Francesco_Ferruccio",
      "aliases": [
        "PISC517_Francesco_Ferruccio",
        "PISC517",
        "3752769264"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": 42.3,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            25
          ],
          "stern": [
            16,
            25
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16,
            20,
            52
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC519_Michelangelo": {
      "name": "PISC519_Michelangelo",
      "aliases": [
        "PISC519_Michelangelo",
        "PISC519",
        "3750672112"
      ],
      "mainGunCaliberMm": 320,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 82.7,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            40,
            100
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC590_Black_Napoli": {
      "name": "PISC590_Black_Napoli",
      "aliases": [
        "PISC590_Black_Napoli",
        "PISC590",
        "3676223216"
      ],
      "mainGunCaliberMm": 254,
      "mainGunHePenMm": 42,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            60
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60
          ],
          "bow": [
            60
          ],
          "stern": [
            60
          ]
        }
      }
    },
    "PISC607_Gorizia": {
      "name": "PISC607_Gorizia",
      "aliases": [
        "PISC607_Gorizia",
        "PISC607",
        "3658397424"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 54.9,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC707_Olympian_Francesco_Ferruccio": {
      "name": "PISC707_Olympian_Francesco_Ferruccio",
      "aliases": [
        "PISC707_Olympian_Francesco_Ferruccio",
        "PISC707",
        "3553539824"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": 42.3,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            25
          ],
          "stern": [
            16,
            25
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16,
            20,
            52
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC710_Varese": {
      "name": "PISC710_Varese",
      "aliases": [
        "PISC710_Varese",
        "PISC710",
        "3550394096"
      ],
      "mainGunCaliberMm": 320,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 82.7,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            40,
            100
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC717_Fiume": {
      "name": "PISC717_Fiume",
      "aliases": [
        "PISC717_Fiume",
        "PISC717",
        "3543054064"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC719_Ferrante_Gonzaga": {
      "name": "PISC719_Ferrante_Gonzaga",
      "aliases": [
        "PISC719_Ferrante_Gonzaga",
        "PISC719",
        "3540956912"
      ],
      "mainGunCaliberMm": 135,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": 38,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            30
          ],
          "bow": [
            30
          ],
          "stern": []
        }
      }
    },
    "PISC729_Messina": {
      "name": "PISC729_Messina",
      "aliases": [
        "PISC729_Messina",
        "PISC729",
        "3530471152"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 42.3,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC897_Azur_Gorizia": {
      "name": "PISC897_Azur_Gorizia",
      "aliases": [
        "PISC897_Azur_Gorizia",
        "PISC897",
        "3354310384"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 54.9,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC908_East_Amalfi": {
      "name": "PISC908_East_Amalfi",
      "aliases": [
        "PISC908_East_Amalfi",
        "PISC908",
        "3342776048"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 54.9,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISC990_Ravenna": {
      "name": "PISC990_Ravenna",
      "aliases": [
        "PISC990_Ravenna",
        "PISC990",
        "3256792816"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 54.9,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30,
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40,
            60
          ],
          "bow": [
            40
          ],
          "stern": [
            40,
            60
          ]
        }
      }
    },
    "PISD102_Curtatone": {
      "name": "PISD102_Curtatone",
      "aliases": [
        "PISD102_Curtatone",
        "PISD102",
        "4187895536"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 29.5,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISD103_Sauro": {
      "name": "PISD103_Sauro",
      "aliases": [
        "PISD103_Sauro",
        "PISD103",
        "4186846960"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": 34.2,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISD104_Turbine": {
      "name": "PISD104_Turbine",
      "aliases": [
        "PISD104_Turbine",
        "PISD104",
        "4185798384"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": 34.2,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISD105_Maestrale": {
      "name": "PISD105_Maestrale",
      "aliases": [
        "PISD105_Maestrale",
        "PISD105",
        "4184749808"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": 34.2,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISD106_Aviere": {
      "name": "PISD106_Aviere",
      "aliases": [
        "PISD106_Aviere",
        "PISD106",
        "4183701232"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": 34.2,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISD107_Luca_Tarigo": {
      "name": "PISD107_Luca_Tarigo",
      "aliases": [
        "PISD107_Luca_Tarigo",
        "PISD107",
        "4182652656"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": 34.2,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISD108_Vittorio_Cuniberti": {
      "name": "PISD108_Vittorio_Cuniberti",
      "aliases": [
        "PISD108_Vittorio_Cuniberti",
        "PISD108",
        "4181604080"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": 34.2,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISD109_Adriatico": {
      "name": "PISD109_Adriatico",
      "aliases": [
        "PISD109_Adriatico",
        "PISD109",
        "4180555504"
      ],
      "mainGunCaliberMm": 135,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": 38,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISD110_Attilio_Regolo": {
      "name": "PISD110_Attilio_Regolo",
      "aliases": [
        "PISD110_Attilio_Regolo",
        "PISD110",
        "4179506928"
      ],
      "mainGunCaliberMm": 135,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": 38,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISD506_Leone": {
      "name": "PISD506_Leone",
      "aliases": [
        "PISD506_Leone",
        "PISD506",
        "3764270832"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISD507_FR25": {
      "name": "PISD507_FR25",
      "aliases": [
        "PISD507_FR25",
        "PISD507",
        "3763222256"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": 39,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISD509_Paolo_Emilio": {
      "name": "PISD509_Paolo_Emilio",
      "aliases": [
        "PISD509_Paolo_Emilio",
        "PISD509",
        "3761125104"
      ],
      "mainGunCaliberMm": 135,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": 38,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            20
          ],
          "stern": [
            19,
            20
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": [
            19,
            60
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISD710_Alberico_da_Barbiano": {
      "name": "PISD710_Alberico_da_Barbiano",
      "aliases": [
        "PISD710_Alberico_da_Barbiano",
        "PISD710",
        "3550361328"
      ],
      "mainGunCaliberMm": 90,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 26,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISS106_Foca": {
      "name": "PISS106_Foca",
      "aliases": [
        "PISS106_Foca",
        "PISS106",
        "4183209712"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            13,
            16
          ],
          "stern": [
            10,
            13,
            16
          ]
        },
        "deck": {
          "values": [
            10,
            13,
            16
          ]
        },
        "side": {
          "values": [
            10,
            13,
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISS108_Pietro_Micca": {
      "name": "PISS108_Pietro_Micca",
      "aliases": [
        "PISS108_Pietro_Micca",
        "PISS108",
        "4181112560"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PISS110_Calvi": {
      "name": "PISS110_Calvi",
      "aliases": [
        "PISS110_Calvi",
        "PISS110",
        "4179015408"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA002_Hosho_1939": {
      "name": "PJSA002_Hosho_1939",
      "aliases": [
        "PJSA002_Hosho_1939",
        "PJSA002",
        "4292851408"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA006_Zuiho_1944": {
      "name": "PJSA006_Zuiho_1944",
      "aliases": [
        "PJSA006_Zuiho_1944",
        "PJSA006",
        "4288657104"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            15
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA009_Ryujo_1933": {
      "name": "PJSA009_Ryujo_1933",
      "aliases": [
        "PJSA009_Ryujo_1933",
        "PJSA009",
        "4285511376"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA011_Hiryu_1942": {
      "name": "PJSA011_Hiryu_1942",
      "aliases": [
        "PJSA011_Hiryu_1942",
        "PJSA011",
        "4283414224"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            67
          ],
          "stern": [
            19,
            67
          ]
        },
        "deck": {
          "values": [
            67
          ]
        },
        "side": {
          "values": [
            19,
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA012_Zuikaku_1944": {
      "name": "PJSA012_Zuikaku_1944",
      "aliases": [
        "PJSA012_Zuikaku_1944",
        "PJSA012",
        "4282365648"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            38
          ],
          "stern": [
            19,
            38
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            215
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA015_Taiho_1944": {
      "name": "PJSA015_Taiho_1944",
      "aliases": [
        "PJSA015_Taiho_1944",
        "PJSA015",
        "4279219920"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19,
            48
          ]
        },
        "deck": {
          "values": [
            95
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA017_Hakuryu_1942": {
      "name": "PJSA017_Hakuryu_1942",
      "aliases": [
        "PJSA017_Hakuryu_1942",
        "PJSA017",
        "4277122768"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            95
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA104_Hosho": {
      "name": "PJSA104_Hosho",
      "aliases": [
        "PJSA104_Hosho",
        "PJSA104",
        "4185896656"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA106_Ryujo": {
      "name": "PJSA106_Ryujo",
      "aliases": [
        "PJSA106_Ryujo",
        "PJSA106",
        "4183799504"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA108_Shokaku": {
      "name": "PJSA108_Shokaku",
      "aliases": [
        "PJSA108_Shokaku",
        "PJSA108",
        "4181702352"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            215
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA110_Hakuryu": {
      "name": "PJSA110_Hakuryu",
      "aliases": [
        "PJSA110_Hakuryu",
        "PJSA110",
        "4179605200"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            95
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA111_Sekiryu": {
      "name": "PJSA111_Sekiryu",
      "aliases": [
        "PJSA111_Sekiryu",
        "PJSA111",
        "4178556624"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            40
          ],
          "stern": [
            19,
            40
          ]
        },
        "deck": {
          "values": [
            40,
            95
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA507_Kaga": {
      "name": "PJSA507_Kaga",
      "aliases": [
        "PJSA507_Kaga",
        "PJSA507",
        "3763320528"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            21
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            120
          ],
          "bow": [
            120
          ],
          "stern": [
            120
          ]
        }
      }
    },
    "PJSA518_Kaga": {
      "name": "PJSA518_Kaga",
      "aliases": [
        "PJSA518_Kaga",
        "PJSA518",
        "3751786192"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            21
          ],
          "stern": [
            21
          ]
        },
        "deck": {
          "values": [
            21
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            120
          ],
          "bow": [
            120
          ],
          "stern": [
            120
          ]
        }
      }
    },
    "PJSA598_Black_Kaga": {
      "name": "PJSA598_Black_Kaga",
      "aliases": [
        "PJSA598_Black_Kaga",
        "PJSA598",
        "3667900112"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            21
          ],
          "stern": [
            21
          ]
        },
        "deck": {
          "values": [
            21
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            120
          ],
          "bow": [
            120
          ],
          "stern": [
            120
          ]
        }
      }
    },
    "PJSA710_Shinano": {
      "name": "PJSA710_Shinano",
      "aliases": [
        "PJSA710_Shinano",
        "PJSA710",
        "3550459600"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            75
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA908_Kikaku": {
      "name": "PJSA908_Kikaku",
      "aliases": [
        "PJSA908_Kikaku",
        "PJSA908",
        "3342841552"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            215
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA910_Taiho": {
      "name": "PJSA910_Taiho",
      "aliases": [
        "PJSA910_Taiho",
        "PJSA910",
        "3340744400"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19,
            48
          ]
        },
        "deck": {
          "values": [
            95
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA917_TST_Hakuryu": {
      "name": "PJSA917_TST_Hakuryu",
      "aliases": [
        "PJSA917_TST_Hakuryu",
        "PJSA917",
        "3333404368"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            95
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSA920_Azur_Shinano": {
      "name": "PJSA920_Azur_Shinano",
      "aliases": [
        "PJSA920_Azur_Shinano",
        "PJSA920",
        "3330258640"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            75
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB001_Kawachi_1912": {
      "name": "PJSB001_Kawachi_1912",
      "aliases": [
        "PJSB001_Kawachi_1912",
        "PJSB001",
        "4293867216"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            152,
            178
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB003_Myogi_1912": {
      "name": "PJSB003_Myogi_1912",
      "aliases": [
        "PJSB003_Myogi_1912",
        "PJSB003",
        "4291770064"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            76
          ],
          "bow": [
            76
          ],
          "stern": []
        }
      }
    },
    "PJSB006_Fuso_1943": {
      "name": "PJSB006_Fuso_1943",
      "aliases": [
        "PJSB006_Fuso_1943",
        "PJSB006",
        "4288624336"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            35
          ]
        },
        "side": {
          "values": [
            152,
            203
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            102
          ],
          "bow": [
            102
          ],
          "stern": []
        }
      }
    },
    "PJSB007_Kongo_1942": {
      "name": "PJSB007_Kongo_1942",
      "aliases": [
        "PJSB007_Kongo_1942",
        "PJSB007",
        "4287575760"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19,
            38
          ]
        },
        "side": {
          "values": [
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB008_Ishizuchi_1921": {
      "name": "PJSB008_Ishizuchi_1921",
      "aliases": [
        "PJSB008_Ishizuchi_1921",
        "PJSB008",
        "4286527184"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            38
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            76
          ],
          "bow": [
            76
          ],
          "stern": []
        }
      }
    },
    "PJSB010_Nagato_1944": {
      "name": "PJSB010_Nagato_1944",
      "aliases": [
        "PJSB010_Nagato_1944",
        "PJSB010",
        "4284430032"
      ],
      "mainGunCaliberMm": 410,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26,
            229
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB011_Mikasa_1905": {
      "name": "PJSB011_Mikasa_1905",
      "aliases": [
        "PJSB011_Mikasa_1905",
        "PJSB011",
        "4283381456"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB013_Amagi_1942": {
      "name": "PJSB013_Amagi_1942",
      "aliases": [
        "PJSB013_Amagi_1942",
        "PJSB013",
        "4281284304"
      ],
      "mainGunCaliberMm": 410,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB018_Yamato_1944": {
      "name": "PJSB018_Yamato_1944",
      "aliases": [
        "PJSB018_Yamato_1944",
        "PJSB018",
        "4276041424"
      ],
      "mainGunCaliberMm": 460,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            57
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB021_Izumo_1938": {
      "name": "PJSB021_Izumo_1938",
      "aliases": [
        "PJSB021_Izumo_1938",
        "PJSB021",
        "4272895696"
      ],
      "mainGunCaliberMm": 410,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            57
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB111_Satsuma": {
      "name": "PJSB111_Satsuma",
      "aliases": [
        "PJSB111_Satsuma",
        "PJSB111",
        "4178523856"
      ],
      "mainGunCaliberMm": 510,
      "mainGunHePenMm": 85,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            45,
            57
          ],
          "stern": [
            32,
            45,
            57
          ]
        },
        "deck": {
          "values": [
            45,
            57
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB208_Yumihari": {
      "name": "PJSB208_Yumihari",
      "aliases": [
        "PJSB208_Yumihari",
        "PJSB208",
        "4076811984"
      ],
      "mainGunCaliberMm": 410,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB209_Adatara": {
      "name": "PJSB209_Adatara",
      "aliases": [
        "PJSB209_Adatara",
        "PJSB209",
        "4075763408"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            32,
            57
          ]
        },
        "side": {
          "values": [
            32,
            102
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            255
          ],
          "bow": [],
          "stern": [
            255
          ]
        }
      }
    },
    "PJSB210_Bungo": {
      "name": "PJSB210_Bungo",
      "aliases": [
        "PJSB210_Bungo",
        "PJSB210",
        "4074714832"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB506_Mutsu": {
      "name": "PJSB506_Mutsu",
      "aliases": [
        "PJSB506_Mutsu",
        "PJSB506",
        "3764336336"
      ],
      "mainGunCaliberMm": 410,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26,
            229
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB507_Ashitaka": {
      "name": "PJSB507_Ashitaka",
      "aliases": [
        "PJSB507_Ashitaka",
        "PJSB507",
        "3763287760"
      ],
      "mainGunCaliberMm": 410,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB508_Kii": {
      "name": "PJSB508_Kii",
      "aliases": [
        "PJSB508_Kii",
        "PJSB508",
        "3762239184"
      ],
      "mainGunCaliberMm": 410,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB509_Musashi": {
      "name": "PJSB509_Musashi",
      "aliases": [
        "PJSB509_Musashi",
        "PJSB509",
        "3761190608"
      ],
      "mainGunCaliberMm": 460,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            57
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB510_Shikishima": {
      "name": "PJSB510_Shikishima",
      "aliases": [
        "PJSB510_Shikishima",
        "PJSB510",
        "3760142032"
      ],
      "mainGunCaliberMm": 510,
      "mainGunHePenMm": 85,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            57
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB517_Hyuga": {
      "name": "PJSB517_Hyuga",
      "aliases": [
        "PJSB517_Hyuga",
        "PJSB517",
        "3752802000"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            35
          ]
        },
        "side": {
          "values": [
            149,
            199
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB519_Hizen": {
      "name": "PJSB519_Hizen",
      "aliases": [
        "PJSB519_Hizen",
        "PJSB519",
        "3750704848"
      ],
      "mainGunCaliberMm": 410,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32,
            45
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB526_Ise": {
      "name": "PJSB526_Ise",
      "aliases": [
        "PJSB526_Ise",
        "PJSB526",
        "3743364816"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26,
            199
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB529_Iwami": {
      "name": "PJSB529_Iwami",
      "aliases": [
        "PJSB529_Iwami",
        "PJSB529",
        "3740219088"
      ],
      "mainGunCaliberMm": 410,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            32,
            45
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB539_Daisen": {
      "name": "PJSB539_Daisen",
      "aliases": [
        "PJSB539_Daisen",
        "PJSB539",
        "3729733328"
      ],
      "mainGunCaliberMm": 410,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB549_Tsurugi": {
      "name": "PJSB549_Tsurugi",
      "aliases": [
        "PJSB549_Tsurugi",
        "PJSB549",
        "3719247568"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB559_Black_Iwami": {
      "name": "PJSB559_Black_Iwami",
      "aliases": [
        "PJSB559_Black_Iwami",
        "PJSB559",
        "3708761808"
      ],
      "mainGunCaliberMm": 410,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            32,
            45
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB700_ARP_Yamato": {
      "name": "PJSB700_ARP_Yamato",
      "aliases": [
        "PJSB700_ARP_Yamato",
        "PJSB700",
        "3560912592"
      ],
      "mainGunCaliberMm": 460,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            57
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB705_Kongou": {
      "name": "PJSB705_Kongou",
      "aliases": [
        "PJSB705_Kongou",
        "PJSB705",
        "3555669712"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19,
            38
          ]
        },
        "side": {
          "values": [
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB706_Kirishima": {
      "name": "PJSB706_Kirishima",
      "aliases": [
        "PJSB706_Kirishima",
        "PJSB706",
        "3554621136"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19,
            38
          ]
        },
        "side": {
          "values": [
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB707_Haruna": {
      "name": "PJSB707_Haruna",
      "aliases": [
        "PJSB707_Haruna",
        "PJSB707",
        "3553572560"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19,
            38
          ]
        },
        "side": {
          "values": [
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB708_Hiei_Arpeggio": {
      "name": "PJSB708_Hiei_Arpeggio",
      "aliases": [
        "PJSB708_Hiei_Arpeggio",
        "PJSB708",
        "3552523984"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19,
            38
          ]
        },
        "side": {
          "values": [
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB710_FBO_Yamato": {
      "name": "PJSB710_FBO_Yamato",
      "aliases": [
        "PJSB710_FBO_Yamato",
        "PJSB710",
        "3550426832"
      ],
      "mainGunCaliberMm": 460,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            57
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB715_HSF_Hiei": {
      "name": "PJSB715_HSF_Hiei",
      "aliases": [
        "PJSB715_HSF_Hiei",
        "PJSB715",
        "3545183952"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19,
            38
          ]
        },
        "side": {
          "values": [
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB719_Hotaka": {
      "name": "PJSB719_Hotaka",
      "aliases": [
        "PJSB719_Hotaka",
        "PJSB719",
        "3540989648"
      ],
      "mainGunCaliberMm": 410,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32,
            57
          ]
        },
        "side": {
          "values": [
            32,
            102
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            255
          ],
          "bow": [],
          "stern": [
            255
          ]
        }
      }
    },
    "PJSB720_Aki": {
      "name": "PJSB720_Aki",
      "aliases": [
        "PJSB720_Aki",
        "PJSB720",
        "3539941072"
      ],
      "mainGunCaliberMm": 460,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            57
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB799_Kirishima": {
      "name": "PJSB799_Kirishima",
      "aliases": [
        "PJSB799_Kirishima",
        "PJSB799",
        "3457103568"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": []
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB878_Ignis_Purgatio": {
      "name": "PJSB878_Ignis_Purgatio",
      "aliases": [
        "PJSB878_Ignis_Purgatio",
        "PJSB878",
        "3374266064"
      ],
      "mainGunCaliberMm": 410,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB888_Ragnarok": {
      "name": "PJSB888_Ragnarok",
      "aliases": [
        "PJSB888_Ragnarok",
        "PJSB888",
        "3363780304"
      ],
      "mainGunCaliberMm": 410,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB891_Satsuma_PLUS": {
      "name": "PJSB891_Satsuma_PLUS",
      "aliases": [
        "PJSB891_Satsuma_PLUS",
        "PJSB891",
        "3360634576"
      ],
      "mainGunCaliberMm": 510,
      "mainGunHePenMm": 85,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            45,
            57
          ],
          "stern": [
            32,
            45,
            57
          ]
        },
        "deck": {
          "values": [
            45,
            57
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB906_Ise_TEST1": {
      "name": "PJSB906_Ise_TEST1",
      "aliases": [
        "PJSB906_Ise_TEST1",
        "PJSB906",
        "3344905936"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26,
            199
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB916_Ise_TEST2": {
      "name": "PJSB916_Ise_TEST2",
      "aliases": [
        "PJSB916_Ise_TEST2",
        "PJSB916",
        "3334420176"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26,
            199
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB918_Yamato_1944": {
      "name": "PJSB918_Yamato_1944",
      "aliases": [
        "PJSB918_Yamato_1944",
        "PJSB918",
        "3332323024"
      ],
      "mainGunCaliberMm": 460,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            57
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB920_Gold_Aki": {
      "name": "PJSB920_Gold_Aki",
      "aliases": [
        "PJSB920_Gold_Aki",
        "PJSB920",
        "3330225872"
      ],
      "mainGunCaliberMm": 460,
      "mainGunHePenMm": 77,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            57
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSB999_Satsuma": {
      "name": "PJSB999_Satsuma",
      "aliases": [
        "PJSB999_Satsuma",
        "PJSB999",
        "3247388368"
      ],
      "mainGunCaliberMm": 510,
      "mainGunHePenMm": 85,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            45,
            57
          ],
          "stern": [
            32,
            45,
            57
          ]
        },
        "deck": {
          "values": [
            45,
            57
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC004_Yubari_1944": {
      "name": "PJSC004_Yubari_1944",
      "aliases": [
        "PJSC004_Yubari_1944",
        "PJSC004",
        "4290688720"
      ],
      "mainGunCaliberMm": 140,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": []
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC005_Furutaka_1926": {
      "name": "PJSC005_Furutaka_1926",
      "aliases": [
        "PJSC005_Furutaka_1926",
        "PJSC005",
        "4289640144"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            48
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC007_Aoba_1943": {
      "name": "PJSC007_Aoba_1943",
      "aliases": [
        "PJSC007_Aoba_1943",
        "PJSC007",
        "4287542992"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            48
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC008_Myoko_1945": {
      "name": "PJSC008_Myoko_1945",
      "aliases": [
        "PJSC008_Myoko_1945",
        "PJSC008",
        "4286494416"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC009_Mogami_1935": {
      "name": "PJSC009_Mogami_1935",
      "aliases": [
        "PJSC009_Mogami_1935",
        "PJSC009",
        "4285445840"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC012_Ibuki_1944": {
      "name": "PJSC012_Ibuki_1944",
      "aliases": [
        "PJSC012_Ibuki_1944",
        "PJSC012",
        "4282300112"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC013_Kuma_1938": {
      "name": "PJSC013_Kuma_1938",
      "aliases": [
        "PJSC013_Kuma_1938",
        "PJSC013",
        "4281251536"
      ],
      "mainGunCaliberMm": 140,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": []
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC014_Kitakami_1945": {
      "name": "PJSC014_Kitakami_1945",
      "aliases": [
        "PJSC014_Kitakami_1945",
        "PJSC014",
        "4280202960"
      ],
      "mainGunCaliberMm": 140,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC015_Tatsuta_1919": {
      "name": "PJSC015_Tatsuta_1919",
      "aliases": [
        "PJSC015_Tatsuta_1919",
        "PJSC015",
        "4279154384"
      ],
      "mainGunCaliberMm": 140,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": []
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC018_Tone": {
      "name": "PJSC018_Tone",
      "aliases": [
        "PJSC018_Tone",
        "PJSC018",
        "4276008656"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25,
            27
          ],
          "stern": [
            25,
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC026_Iwaki_1944": {
      "name": "PJSC026_Iwaki_1944",
      "aliases": [
        "PJSC026_Iwaki_1944",
        "PJSC026",
        "4267620048"
      ],
      "mainGunCaliberMm": 140,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": []
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC034_Zao_1944": {
      "name": "PJSC034_Zao_1944",
      "aliases": [
        "PJSC034_Zao_1944",
        "PJSC034",
        "4259231440"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC035_Chikuma_1912": {
      "name": "PJSC035_Chikuma_1912",
      "aliases": [
        "PJSC035_Chikuma_1912",
        "PJSC035",
        "4258182864"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": [
            13,
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC037_Hashidate_1940": {
      "name": "PJSC037_Hashidate_1940",
      "aliases": [
        "PJSC037_Hashidate_1940",
        "PJSC037",
        "4256085712"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10,
            13
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC038_Atago_1944": {
      "name": "PJSC038_Atago_1944",
      "aliases": [
        "PJSC038_Atago_1944",
        "PJSC038",
        "4255037136"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            41
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC205_Agano": {
      "name": "PJSC205_Agano",
      "aliases": [
        "PJSC205_Agano",
        "PJSC205",
        "4079924944"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC206_Gokase": {
      "name": "PJSC206_Gokase",
      "aliases": [
        "PJSC206_Gokase",
        "PJSC206",
        "4078876368"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC207_Omono": {
      "name": "PJSC207_Omono",
      "aliases": [
        "PJSC207_Omono",
        "PJSC207",
        "4077827792"
      ],
      "mainGunCaliberMm": 155,
      "mainGunHePenMm": 26,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC208_Shimanto": {
      "name": "PJSC208_Shimanto",
      "aliases": [
        "PJSC208_Shimanto",
        "PJSC208",
        "4076779216"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC209_Takahashi": {
      "name": "PJSC209_Takahashi",
      "aliases": [
        "PJSC209_Takahashi",
        "PJSC209",
        "4075730640"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC210_Yodo": {
      "name": "PJSC210_Yodo",
      "aliases": [
        "PJSC210_Yodo",
        "PJSC210",
        "4074682064"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC503_Katori": {
      "name": "PJSC503_Katori",
      "aliases": [
        "PJSC503_Katori",
        "PJSC503",
        "3767449296"
      ],
      "mainGunCaliberMm": 140,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC505_Yahagi": {
      "name": "PJSC505_Yahagi",
      "aliases": [
        "PJSC505_Yahagi",
        "PJSC505",
        "3765352144"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC507_Tokachi": {
      "name": "PJSC507_Tokachi",
      "aliases": [
        "PJSC507_Tokachi",
        "PJSC507",
        "3763254992"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            48
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC510_Azumaya": {
      "name": "PJSC510_Azumaya",
      "aliases": [
        "PJSC510_Azumaya",
        "PJSC510",
        "3760109264"
      ],
      "mainGunCaliberMm": 310,
      "mainGunHePenMm": 52,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC517_Maya": {
      "name": "PJSC517_Maya",
      "aliases": [
        "PJSC517_Maya",
        "PJSC517",
        "3752769232"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            29
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC519_AZUR_Azuma": {
      "name": "PJSC519_AZUR_Azuma",
      "aliases": [
        "PJSC519_AZUR_Azuma",
        "PJSC519",
        "3750672080"
      ],
      "mainGunCaliberMm": 310,
      "mainGunHePenMm": 52,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC520_Yoshino": {
      "name": "PJSC520_Yoshino",
      "aliases": [
        "PJSC520_Yoshino",
        "PJSC520",
        "3749623504"
      ],
      "mainGunCaliberMm": 310,
      "mainGunHePenMm": 52,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC590_Black_Yoshino": {
      "name": "PJSC590_Black_Yoshino",
      "aliases": [
        "PJSC590_Black_Yoshino",
        "PJSC590",
        "3676223184"
      ],
      "mainGunCaliberMm": 310,
      "mainGunHePenMm": 52,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC598_Black_Atago": {
      "name": "PJSC598_Black_Atago",
      "aliases": [
        "PJSC598_Black_Atago",
        "PJSC598",
        "3667834576"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            41
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC610_Kitakami": {
      "name": "PJSC610_Kitakami",
      "aliases": [
        "PJSC610_Kitakami",
        "PJSC610",
        "3655251664"
      ],
      "mainGunCaliberMm": 140,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC705_Myoko": {
      "name": "PJSC705_Myoko",
      "aliases": [
        "PJSC705_Myoko",
        "PJSC705",
        "3555636944"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC707_Ashigara": {
      "name": "PJSC707_Ashigara",
      "aliases": [
        "PJSC707_Ashigara",
        "PJSC707",
        "3553539792"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC708_ARP_Takao": {
      "name": "PJSC708_ARP_Takao",
      "aliases": [
        "PJSC708_ARP_Takao",
        "PJSC708",
        "3552491216"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            41
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC709_Haguro": {
      "name": "PJSC709_Haguro",
      "aliases": [
        "PJSC709_Haguro",
        "PJSC709",
        "3551442640"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC710_Yari": {
      "name": "PJSC710_Yari",
      "aliases": [
        "PJSC710_Yari",
        "PJSC710",
        "3550394064"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC717_Yellow_Dragon": {
      "name": "PJSC717_Yellow_Dragon",
      "aliases": [
        "PJSC717_Yellow_Dragon",
        "PJSC717",
        "3543054032"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC718_ARP_Maya": {
      "name": "PJSC718_ARP_Maya",
      "aliases": [
        "PJSC718_ARP_Maya",
        "PJSC718",
        "3542005456"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            41
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC719_Chikuma_2_Hyb": {
      "name": "PJSC719_Chikuma_2_Hyb",
      "aliases": [
        "PJSC719_Chikuma_2_Hyb",
        "PJSC719",
        "3540956880"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25,
            27
          ],
          "stern": [
            25,
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC720_Kushiro": {
      "name": "PJSC720_Kushiro",
      "aliases": [
        "PJSC720_Kushiro",
        "PJSC720",
        "3539908304"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC727_Blue_Dragon": {
      "name": "PJSC727_Blue_Dragon",
      "aliases": [
        "PJSC727_Blue_Dragon",
        "PJSC727",
        "3532568272"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC729_GW_Chikuma_2_Hyb": {
      "name": "PJSC729_GW_Chikuma_2_Hyb",
      "aliases": [
        "PJSC729_GW_Chikuma_2_Hyb",
        "PJSC729",
        "3530471120"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25,
            27
          ],
          "stern": [
            25,
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC737_Nachi": {
      "name": "PJSC737_Nachi",
      "aliases": [
        "PJSC737_Nachi",
        "PJSC737",
        "3522082512"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC739_Suzuya": {
      "name": "PJSC739_Suzuya",
      "aliases": [
        "PJSC739_Suzuya",
        "PJSC739",
        "3519985360"
      ],
      "mainGunCaliberMm": 155,
      "mainGunHePenMm": 31,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC749_GM_Suzuya": {
      "name": "PJSC749_GM_Suzuya",
      "aliases": [
        "PJSC749_GM_Suzuya",
        "PJSC749",
        "3509499600"
      ],
      "mainGunCaliberMm": 155,
      "mainGunHePenMm": 31,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC759_VL_Suzuya": {
      "name": "PJSC759_VL_Suzuya",
      "aliases": [
        "PJSC759_VL_Suzuya",
        "PJSC759",
        "3499013840"
      ],
      "mainGunCaliberMm": 155,
      "mainGunHePenMm": 31,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC810_TST_ZAO": {
      "name": "PJSC810_TST_ZAO",
      "aliases": [
        "PJSC810_TST_ZAO",
        "PJSC810",
        "3445536464"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC819_BA_Takahashi": {
      "name": "PJSC819_BA_Takahashi",
      "aliases": [
        "PJSC819_BA_Takahashi",
        "PJSC819",
        "3436099280"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC829_Black_Azumaya": {
      "name": "PJSC829_Black_Azumaya",
      "aliases": [
        "PJSC829_Black_Azumaya",
        "PJSC829",
        "3425613520"
      ],
      "mainGunCaliberMm": 310,
      "mainGunHePenMm": 52,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC890_CLR_Zao": {
      "name": "PJSC890_CLR_Zao",
      "aliases": [
        "PJSC890_CLR_Zao",
        "PJSC890",
        "3361650384"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC905_East_Furutaka_1926": {
      "name": "PJSC905_East_Furutaka_1926",
      "aliases": [
        "PJSC905_East_Furutaka_1926",
        "PJSC905",
        "3345921744"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            48
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC918_Tone_Second": {
      "name": "PJSC918_Tone_Second",
      "aliases": [
        "PJSC918_Tone_Second",
        "PJSC918",
        "3332290256"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25,
            27
          ],
          "stern": [
            25,
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC919_Tone_Third": {
      "name": "PJSC919_Tone_Third",
      "aliases": [
        "PJSC919_Tone_Third",
        "PJSC919",
        "3331241680"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25,
            27
          ],
          "stern": [
            25,
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSC934_Zao_1944": {
      "name": "PJSC934_Zao_1944",
      "aliases": [
        "PJSC934_Zao_1944",
        "PJSC934",
        "3315513040"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD001_Tachibana_1912": {
      "name": "PJSD001_Tachibana_1912",
      "aliases": [
        "PJSD001_Tachibana_1912",
        "PJSD001",
        "4293801680"
      ],
      "mainGunCaliberMm": 76,
      "mainGunHePenMm": 13,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD002_Umikaze_1925": {
      "name": "PJSD002_Umikaze_1925",
      "aliases": [
        "PJSD002_Umikaze_1925",
        "PJSD002",
        "4292753104"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD003_Isokaze_1917": {
      "name": "PJSD003_Isokaze_1917",
      "aliases": [
        "PJSD003_Isokaze_1917",
        "PJSD003",
        "4291704528"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            14
          ],
          "stern": [
            10,
            14
          ]
        },
        "deck": {
          "values": [
            14
          ]
        },
        "side": {
          "values": [
            14
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD004_Minekadze_1920": {
      "name": "PJSD004_Minekadze_1920",
      "aliases": [
        "PJSD004_Minekadze_1920",
        "PJSD004",
        "4290655952"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            14
          ],
          "stern": [
            10,
            12,
            14
          ]
        },
        "deck": {
          "values": [
            14
          ]
        },
        "side": {
          "values": [
            14
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD005_Mutsuki_1926": {
      "name": "PJSD005_Mutsuki_1926",
      "aliases": [
        "PJSD005_Mutsuki_1926",
        "PJSD005",
        "4289607376"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            14,
            16
          ],
          "stern": [
            14,
            16
          ]
        },
        "deck": {
          "values": [
            14
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD006_Hatsuharu_1945": {
      "name": "PJSD006_Hatsuharu_1945",
      "aliases": [
        "PJSD006_Hatsuharu_1945",
        "PJSD006",
        "4288558800"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            15,
            16
          ],
          "stern": [
            15,
            16
          ]
        },
        "deck": {
          "values": [
            15
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD007_Fubuki_1944": {
      "name": "PJSD007_Fubuki_1944",
      "aliases": [
        "PJSD007_Fubuki_1944",
        "PJSD007",
        "4287510224"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            15,
            19
          ],
          "stern": [
            15,
            19
          ]
        },
        "deck": {
          "values": [
            15
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD010_Kagero_1943": {
      "name": "PJSD010_Kagero_1943",
      "aliases": [
        "PJSD010_Kagero_1943",
        "PJSD010",
        "4284364496"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            15,
            19
          ],
          "stern": [
            15,
            19
          ]
        },
        "deck": {
          "values": [
            15
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD012_Shimakaze_1943": {
      "name": "PJSD012_Shimakaze_1943",
      "aliases": [
        "PJSD012_Shimakaze_1943",
        "PJSD012",
        "4282267344"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD014_Tachibana_1912_Asus": {
      "name": "PJSD014_Tachibana_1912_Asus",
      "aliases": [
        "PJSD014_Tachibana_1912_Asus",
        "PJSD014",
        "4280170192"
      ],
      "mainGunCaliberMm": 76,
      "mainGunHePenMm": 13,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD017_Kamikaze_1930": {
      "name": "PJSD017_Kamikaze_1930",
      "aliases": [
        "PJSD017_Kamikaze_1930",
        "PJSD017",
        "4277024464"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            14
          ],
          "stern": [
            10,
            12,
            14
          ]
        },
        "deck": {
          "values": [
            14
          ]
        },
        "side": {
          "values": [
            14
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD024_Wakatake_1923": {
      "name": "PJSD024_Wakatake_1923",
      "aliases": [
        "PJSD024_Wakatake_1923",
        "PJSD024",
        "4269684432"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            12
          ],
          "stern": [
            12
          ]
        },
        "deck": {
          "values": [
            12
          ]
        },
        "side": {
          "values": [
            12
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD025_True_Kamikaze": {
      "name": "PJSD025_True_Kamikaze",
      "aliases": [
        "PJSD025_True_Kamikaze",
        "PJSD025",
        "4268635856"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            14
          ],
          "stern": [
            10,
            12,
            14
          ]
        },
        "deck": {
          "values": [
            14
          ]
        },
        "side": {
          "values": [
            14
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD026_Camo_Kamikaze": {
      "name": "PJSD026_Camo_Kamikaze",
      "aliases": [
        "PJSD026_Camo_Kamikaze",
        "PJSD026",
        "4267587280"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            14
          ],
          "stern": [
            10,
            12,
            14
          ]
        },
        "deck": {
          "values": [
            14
          ]
        },
        "side": {
          "values": [
            14
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD105_Mutsuki": {
      "name": "PJSD105_Mutsuki",
      "aliases": [
        "PJSD105_Mutsuki",
        "PJSD105",
        "4184749776"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            14
          ],
          "stern": [
            10,
            12,
            14
          ]
        },
        "deck": {
          "values": [
            14
          ]
        },
        "side": {
          "values": [
            14
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD106_Fubuki": {
      "name": "PJSD106_Fubuki",
      "aliases": [
        "PJSD106_Fubuki",
        "PJSD106",
        "4183701200"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD107_Akatsuki": {
      "name": "PJSD107_Akatsuki",
      "aliases": [
        "PJSD107_Akatsuki",
        "PJSD107",
        "4182652624"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD108_Akizuki": {
      "name": "PJSD108_Akizuki",
      "aliases": [
        "PJSD108_Akizuki",
        "PJSD108",
        "4181604048"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19,
            20
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD111_Yamagiri": {
      "name": "PJSD111_Yamagiri",
      "aliases": [
        "PJSD111_Yamagiri",
        "PJSD111",
        "4178458320"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD206_Hatsuharu": {
      "name": "PJSD206_Hatsuharu",
      "aliases": [
        "PJSD206_Hatsuharu",
        "PJSD206",
        "4078843600"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD207_Shiratsuyu": {
      "name": "PJSD207_Shiratsuyu",
      "aliases": [
        "PJSD207_Shiratsuyu",
        "PJSD207",
        "4077795024"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD208_Kagero": {
      "name": "PJSD208_Kagero",
      "aliases": [
        "PJSD208_Kagero",
        "PJSD208",
        "4076746448"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD209_Yugumo": {
      "name": "PJSD209_Yugumo",
      "aliases": [
        "PJSD209_Yugumo",
        "PJSD209",
        "4075697872"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19,
            20
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD210_Harugumo": {
      "name": "PJSD210_Harugumo",
      "aliases": [
        "PJSD210_Harugumo",
        "PJSD210",
        "4074649296"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD219_Kitakaze": {
      "name": "PJSD219_Kitakaze",
      "aliases": [
        "PJSD219_Kitakaze",
        "PJSD219",
        "4065212112"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD507_Yudachi": {
      "name": "PJSD507_Yudachi",
      "aliases": [
        "PJSD507_Yudachi",
        "PJSD507",
        "3763222224"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD510_Hayate": {
      "name": "PJSD510_Hayate",
      "aliases": [
        "PJSD510_Hayate",
        "PJSD510",
        "3760076496"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD518_Asashio": {
      "name": "PJSD518_Asashio",
      "aliases": [
        "PJSD518_Asashio",
        "PJSD518",
        "3751687888"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD528_Harekaze_2": {
      "name": "PJSD528_Harekaze_2",
      "aliases": [
        "PJSD528_Harekaze_2",
        "PJSD528",
        "3741202128"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD596_Black_Shinonome": {
      "name": "PJSD596_Black_Shinonome",
      "aliases": [
        "PJSD596_Black_Shinonome",
        "PJSD596",
        "3669898960"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD598_Black_Asashio": {
      "name": "PJSD598_Black_Asashio",
      "aliases": [
        "PJSD598_Black_Asashio",
        "PJSD598",
        "3667801808"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD706_Shinonome": {
      "name": "PJSD706_Shinonome",
      "aliases": [
        "PJSD706_Shinonome",
        "PJSD706",
        "3554555600"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD708_HSF_Harekaze": {
      "name": "PJSD708_HSF_Harekaze",
      "aliases": [
        "PJSD708_HSF_Harekaze",
        "PJSD708",
        "3552458448"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD718_AZUR_Yukikaze": {
      "name": "PJSD718_AZUR_Yukikaze",
      "aliases": [
        "PJSD718_AZUR_Yukikaze",
        "PJSD718",
        "3541972688"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD719_Minegumo": {
      "name": "PJSD719_Minegumo",
      "aliases": [
        "PJSD719_Minegumo",
        "PJSD719",
        "3540924112"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD728_Shigure": {
      "name": "PJSD728_Shigure",
      "aliases": [
        "PJSD728_Shigure",
        "PJSD728",
        "3531486928"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19,
            20
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD889_Kitakaze_PR": {
      "name": "PJSD889_Kitakaze_PR",
      "aliases": [
        "PJSD889_Kitakaze_PR",
        "PJSD889",
        "3362666192"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD890_AZUR_Shimakaze": {
      "name": "PJSD890_AZUR_Shimakaze",
      "aliases": [
        "PJSD890_AZUR_Shimakaze",
        "PJSD890",
        "3361617616"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD891_Yamagiri_PLUS": {
      "name": "PJSD891_Yamagiri_PLUS",
      "aliases": [
        "PJSD891_Yamagiri_PLUS",
        "PJSD891",
        "3360569040"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSD912_Shimakaze_1943": {
      "name": "PJSD912_Shimakaze_1943",
      "aliases": [
        "PJSD912_Shimakaze_1943",
        "PJSD912",
        "3338548944"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSS508_I58": {
      "name": "PJSS508_I58",
      "aliases": [
        "PJSS508_I58",
        "PJSS508",
        "3761682128"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSS518_I56": {
      "name": "PJSS518_I56",
      "aliases": [
        "PJSS518_I56",
        "PJSS518",
        "3751196368"
      ],
      "mainGunCaliberMm": 140,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 39.3,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSS720_I56_1944": {
      "name": "PJSS720_I56_1944",
      "aliases": [
        "PJSS720_I56_1944",
        "PJSS720",
        "3539384016"
      ],
      "mainGunCaliberMm": 140,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSS820_BA_I56": {
      "name": "PJSS820_BA_I56",
      "aliases": [
        "PJSS820_BA_I56",
        "PJSS820",
        "3434526416"
      ],
      "mainGunCaliberMm": 140,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSX701_Support": {
      "name": "PJSX701_Support",
      "aliases": [
        "PJSX701_Support",
        "PJSX701",
        "3559143120"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": []
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PJSX702_Support": {
      "name": "PJSX702_Support",
      "aliases": [
        "PJSX702_Support",
        "PJSX702",
        "3558094544"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": []
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSA104_Komsomolets": {
      "name": "PRSA104_Komsomolets",
      "aliases": [
        "PRSA104_Komsomolets",
        "PRSA104",
        "4185896400"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13,
            16
          ],
          "stern": [
            16,
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSA106_Serov": {
      "name": "PRSA106_Serov",
      "aliases": [
        "PRSA106_Serov",
        "PRSA106",
        "4183799248"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19
          ],
          "stern": [
            16,
            19
          ]
        },
        "deck": {
          "values": [
            21
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSA108_Pobeda": {
      "name": "PRSA108_Pobeda",
      "aliases": [
        "PRSA108_Pobeda",
        "PRSA108",
        "4181702096"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            100,
            125
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSA110_Admiral_Nakhimov": {
      "name": "PRSA110_Admiral_Nakhimov",
      "aliases": [
        "PRSA110_Admiral_Nakhimov",
        "PRSA110",
        "4179604944"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            125,
            150
          ],
          "bow": [
            125,
            150
          ],
          "stern": [
            125,
            150
          ]
        }
      }
    },
    "PRSA508_Chkalov": {
      "name": "PRSA508_Chkalov",
      "aliases": [
        "PRSA508_Chkalov",
        "PRSA508",
        "3762271696"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            30
          ],
          "stern": [
            15,
            19,
            21,
            30
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSA598_Black_Chkalov": {
      "name": "PRSA598_Black_Chkalov",
      "aliases": [
        "PRSA598_Black_Chkalov",
        "PRSA598",
        "3667899856"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            30
          ],
          "stern": [
            15,
            19,
            21,
            30
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSA990_Admiral_Orlov": {
      "name": "PRSA990_Admiral_Orlov",
      "aliases": [
        "PRSA990_Admiral_Orlov",
        "PRSA990",
        "3256858064"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            125,
            150
          ],
          "bow": [
            125,
            150
          ],
          "stern": [
            125,
            150
          ]
        }
      }
    },
    "PRSB001_Nikolay_I": {
      "name": "PRSB001_Nikolay_I",
      "aliases": [
        "PRSB001_Nikolay_I",
        "PRSB001",
        "4293866960"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            35
          ]
        },
        "side": {
          "values": [
            75
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            100,
            200
          ],
          "bow": [
            100,
            200
          ],
          "stern": []
        }
      }
    },
    "PRSB103_Knyaz_Suvorov": {
      "name": "PRSB103_Knyaz_Suvorov",
      "aliases": [
        "PRSB103_Knyaz_Suvorov",
        "PRSB103",
        "4186912208"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            102
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            102,
            127
          ],
          "bow": [
            102,
            127
          ],
          "stern": [
            102,
            127
          ]
        }
      }
    },
    "PRSB104_Gangut": {
      "name": "PRSB104_Gangut",
      "aliases": [
        "PRSB104_Gangut",
        "PRSB104",
        "4185863632"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25,
            38
          ],
          "stern": [
            19,
            38
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            125
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50,
            75,
            100,
            125,
            225
          ],
          "bow": [
            75,
            125,
            225
          ],
          "stern": [
            50,
            100
          ]
        }
      }
    },
    "PRSB105_Pyotr_Velikiy": {
      "name": "PRSB105_Pyotr_Velikiy",
      "aliases": [
        "PRSB105_Pyotr_Velikiy",
        "PRSB105",
        "4184815056"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            125
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            75,
            125,
            180
          ],
          "bow": [
            75,
            125,
            180
          ],
          "stern": [
            75,
            180
          ]
        }
      }
    },
    "PRSB106_Izmail": {
      "name": "PRSB106_Izmail",
      "aliases": [
        "PRSB106_Izmail",
        "PRSB106",
        "4183766480"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            12,
            26
          ]
        },
        "side": {
          "values": [
            100
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            113,
            125,
            181
          ],
          "bow": [
            113,
            125,
            181
          ],
          "stern": []
        }
      }
    },
    "PRSB107_Sinop": {
      "name": "PRSB107_Sinop",
      "aliases": [
        "PRSB107_Sinop",
        "PRSB107",
        "4182717904"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26,
            35
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            75,
            100
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            113,
            125,
            200
          ],
          "bow": [
            113,
            125,
            200
          ],
          "stern": [
            113,
            125
          ]
        }
      }
    },
    "PRSB108_Vladivostok": {
      "name": "PRSB108_Vladivostok",
      "aliases": [
        "PRSB108_Vladivostok",
        "PRSB108",
        "4181669328"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            200
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            200
          ],
          "bow": [
            200
          ],
          "stern": [
            200
          ]
        }
      }
    },
    "PRSB109_Sovetsky_Soyuz": {
      "name": "PRSB109_Sovetsky_Soyuz",
      "aliases": [
        "PRSB109_Sovetsky_Soyuz",
        "PRSB109",
        "4180620752"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32,
            40,
            60
          ]
        },
        "deck": {
          "values": [
            60
          ]
        },
        "side": {
          "values": [
            60,
            375
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            180,
            220,
            375,
            420
          ],
          "bow": [
            220,
            420
          ],
          "stern": [
            180,
            375
          ]
        }
      }
    },
    "PRSB110_Sovetskaya_Rossiya": {
      "name": "PRSB110_Sovetskaya_Rossiya",
      "aliases": [
        "PRSB110_Sovetskaya_Rossiya",
        "PRSB110",
        "4179572176"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            60
          ]
        },
        "side": {
          "values": [
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            150,
            300
          ],
          "bow": [
            60,
            150
          ],
          "stern": [
            150,
            300
          ]
        }
      }
    },
    "PRSB111_Admiral_Ushakov": {
      "name": "PRSB111_Admiral_Ushakov",
      "aliases": [
        "PRSB111_Admiral_Ushakov",
        "PRSB111",
        "4178523600"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            60
          ]
        },
        "side": {
          "values": [
            150,
            425,
            450
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            180,
            300
          ],
          "bow": [
            60,
            180
          ],
          "stern": [
            60,
            180,
            300
          ]
        }
      }
    },
    "PRSB505_Oktyabrskaya_Revolutsiya": {
      "name": "PRSB505_Oktyabrskaya_Revolutsiya",
      "aliases": [
        "PRSB505_Oktyabrskaya_Revolutsiya",
        "PRSB505",
        "3765384656"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            38
          ],
          "stern": [
            19,
            32,
            38,
            50
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            125
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            75,
            100,
            125,
            225
          ],
          "bow": [
            75,
            125,
            225
          ],
          "stern": [
            100
          ]
        }
      }
    },
    "PRSB508_Poltava": {
      "name": "PRSB508_Poltava",
      "aliases": [
        "PRSB508_Poltava",
        "PRSB508",
        "3762238928"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            200
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            200
          ],
          "bow": [
            200
          ],
          "stern": [
            200
          ]
        }
      }
    },
    "PRSB509_Navarin": {
      "name": "PRSB509_Navarin",
      "aliases": [
        "PRSB509_Navarin",
        "PRSB509",
        "3761190352"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            35
          ]
        },
        "side": {
          "values": [
            75
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            113,
            125,
            181
          ],
          "bow": [
            113,
            125,
            181
          ],
          "stern": [
            125
          ]
        }
      }
    },
    "PRSB510_Slava": {
      "name": "PRSB510_Slava",
      "aliases": [
        "PRSB510_Slava",
        "PRSB510",
        "3760141776"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            100,
            300
          ],
          "bow": [
            100
          ],
          "stern": [
            100,
            300
          ]
        }
      }
    },
    "PRSB516_Novorossiysk": {
      "name": "PRSB516_Novorossiysk",
      "aliases": [
        "PRSB516_Novorossiysk",
        "PRSB516",
        "3753850320"
      ],
      "mainGunCaliberMm": 320,
      "mainGunHePenMm": 55,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            26,
            43
          ]
        },
        "side": {
          "values": [
            130
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            110
          ],
          "bow": [
            110
          ],
          "stern": []
        }
      }
    },
    "PRSB518_Lenin": {
      "name": "PRSB518_Lenin",
      "aliases": [
        "PRSB518_Lenin",
        "PRSB518",
        "3751753168"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            45
          ]
        },
        "side": {
          "values": [
            50,
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSB528_Borodino": {
      "name": "PRSB528_Borodino",
      "aliases": [
        "PRSB528_Borodino",
        "PRSB528",
        "3741267408"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50,
            100
          ],
          "bow": [
            50,
            100
          ],
          "stern": [
            50
          ]
        }
      }
    },
    "PRSB538_V_I_Lenin": {
      "name": "PRSB538_V_I_Lenin",
      "aliases": [
        "PRSB538_V_I_Lenin",
        "PRSB538",
        "3730781648"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            45
          ]
        },
        "side": {
          "values": [
            50,
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSB709_AZUR_Sov_Russia": {
      "name": "PRSB709_AZUR_Sov_Russia",
      "aliases": [
        "PRSB709_AZUR_Sov_Russia",
        "PRSB709",
        "3551475152"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32,
            40,
            60
          ]
        },
        "deck": {
          "values": [
            60
          ]
        },
        "side": {
          "values": [
            60,
            375
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            180,
            220,
            375,
            420
          ],
          "bow": [
            220,
            420
          ],
          "stern": [
            180,
            375
          ]
        }
      }
    },
    "PRSB710_Sibir": {
      "name": "PRSB710_Sibir",
      "aliases": [
        "PRSB710_Sibir",
        "PRSB710",
        "3550426576"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            150,
            300
          ],
          "bow": [
            60,
            150
          ],
          "stern": [
            150,
            300
          ]
        }
      }
    },
    "PRSB717_Arkhangelsk": {
      "name": "PRSB717_Arkhangelsk",
      "aliases": [
        "PRSB717_Arkhangelsk",
        "PRSB717",
        "3543086544"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            152
          ],
          "bow": [
            152
          ],
          "stern": [
            152
          ]
        }
      }
    },
    "PRSB719_Zarya_Svobody": {
      "name": "PRSB719_Zarya_Svobody",
      "aliases": [
        "PRSB719_Zarya_Svobody",
        "PRSB719",
        "3540989392"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            254
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            254
          ],
          "bow": [
            254
          ],
          "stern": [
            254
          ]
        }
      }
    },
    "PRSB818_Borodino_TE": {
      "name": "PRSB818_Borodino_TE",
      "aliases": [
        "PRSB818_Borodino_TE",
        "PRSB818",
        "3437180368"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50,
            100
          ],
          "bow": [
            50,
            100
          ],
          "stern": [
            50
          ]
        }
      }
    },
    "PRSB819_BA_Zarya_Svobody": {
      "name": "PRSB819_BA_Zarya_Svobody",
      "aliases": [
        "PRSB819_BA_Zarya_Svobody",
        "PRSB819",
        "3436131792"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            254
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            254
          ],
          "bow": [
            254
          ],
          "stern": [
            254
          ]
        }
      }
    },
    "PRSB909_East_Navarin": {
      "name": "PRSB909_East_Navarin",
      "aliases": [
        "PRSB909_East_Navarin",
        "PRSB909",
        "3341759952"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            35
          ]
        },
        "side": {
          "values": [
            75
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            113,
            125,
            181
          ],
          "bow": [
            113,
            125,
            181
          ],
          "stern": [
            125
          ]
        }
      }
    },
    "PRSC001_Avrora_1917": {
      "name": "PRSC001_Avrora_1917",
      "aliases": [
        "PRSC001_Avrora_1917",
        "PRSC001",
        "4293834192"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6,
            9
          ]
        },
        "deck": {
          "values": [
            51
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC002_Diana_1905": {
      "name": "PRSC002_Diana_1905",
      "aliases": [
        "PRSC002_Diana_1905",
        "PRSC002",
        "4292785616"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6,
            9
          ]
        },
        "deck": {
          "values": [
            51
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC003_Murmansk_1944": {
      "name": "PRSC003_Murmansk_1944",
      "aliases": [
        "PRSC003_Murmansk_1944",
        "PRSC003",
        "4291737040"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC010_Diana_1905_Asus": {
      "name": "PRSC010_Diana_1905_Asus",
      "aliases": [
        "PRSC010_Diana_1905_Asus",
        "PRSC010",
        "4284397008"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6,
            9
          ]
        },
        "deck": {
          "values": [
            51
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC101_Orlan": {
      "name": "PRSC101_Orlan",
      "aliases": [
        "PRSC101_Orlan",
        "PRSC101",
        "4188976592"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC102_Novik": {
      "name": "PRSC102_Novik",
      "aliases": [
        "PRSC102_Novik",
        "PRSC102",
        "4187928016"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC103_Bogatyr": {
      "name": "PRSC103_Bogatyr",
      "aliases": [
        "PRSC103_Bogatyr",
        "PRSC103",
        "4186879440"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25,
            80
          ],
          "stern": [
            25,
            80
          ]
        },
        "deck": {
          "values": [
            11,
            25
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC104_Svetlana": {
      "name": "PRSC104_Svetlana",
      "aliases": [
        "PRSC104_Svetlana",
        "PRSC104",
        "4185830864"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13,
            20
          ],
          "stern": [
            20
          ]
        },
        "deck": {
          "values": [
            20,
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            25
          ],
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        }
      }
    },
    "PRSC105_Kirov": {
      "name": "PRSC105_Kirov",
      "aliases": [
        "PRSC105_Kirov",
        "PRSC105",
        "4184782288"
      ],
      "mainGunCaliberMm": 180,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            18
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC106_Pr_94_Budeny": {
      "name": "PRSC106_Pr_94_Budeny",
      "aliases": [
        "PRSC106_Pr_94_Budeny",
        "PRSC106",
        "4183733712"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC107_Schors": {
      "name": "PRSC107_Schors",
      "aliases": [
        "PRSC107_Schors",
        "PRSC107",
        "4182685136"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            20
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC108_Pr_68_Chapaev": {
      "name": "PRSC108_Pr_68_Chapaev",
      "aliases": [
        "PRSC108_Pr_68_Chapaev",
        "PRSC108",
        "4181636560"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC109_Dmitry_Donskoy": {
      "name": "PRSC109_Dmitry_Donskoy",
      "aliases": [
        "PRSC109_Dmitry_Donskoy",
        "PRSC109",
        "4180587984"
      ],
      "mainGunCaliberMm": 180,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC110_Pr_66_Moskva": {
      "name": "PRSC110_Pr_66_Moskva",
      "aliases": [
        "PRSC110_Pr_66_Moskva",
        "PRSC110",
        "4179539408"
      ],
      "mainGunCaliberMm": 220,
      "mainGunHePenMm": 37,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50,
            155
          ],
          "bow": [
            50
          ],
          "stern": [
            50,
            155
          ]
        }
      }
    },
    "PRSC111_Novosibirsk": {
      "name": "PRSC111_Novosibirsk",
      "aliases": [
        "PRSC111_Novosibirsk",
        "PRSC111",
        "4178490832"
      ],
      "mainGunCaliberMm": 254,
      "mainGunHePenMm": 42,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            35
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40,
            130,
            210
          ],
          "bow": [
            40,
            210
          ],
          "stern": [
            40,
            130,
            210
          ]
        }
      }
    },
    "PRSC208_Tallin": {
      "name": "PRSC208_Tallin",
      "aliases": [
        "PRSC208_Tallin",
        "PRSC208",
        "4076778960"
      ],
      "mainGunCaliberMm": 180,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40,
            70
          ],
          "bow": [
            40
          ],
          "stern": [
            70
          ]
        }
      }
    },
    "PRSC209_Riga": {
      "name": "PRSC209_Riga",
      "aliases": [
        "PRSC209_Riga",
        "PRSC209",
        "4075730384"
      ],
      "mainGunCaliberMm": 220,
      "mainGunHePenMm": 37,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            35
          ]
        },
        "side": {
          "values": [
            35
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40,
            130
          ],
          "bow": [
            40
          ],
          "stern": [
            40,
            130
          ]
        }
      }
    },
    "PRSC210_Pr_84_Alexander_Nevsky": {
      "name": "PRSC210_Pr_84_Alexander_Nevsky",
      "aliases": [
        "PRSC210_Pr_84_Alexander_Nevsky",
        "PRSC210",
        "4074681808"
      ],
      "mainGunCaliberMm": 180,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50
          ],
          "bow": [
            50
          ],
          "stern": [
            50
          ]
        }
      }
    },
    "PRSC215_Kotovsky": {
      "name": "PRSC215_Kotovsky",
      "aliases": [
        "PRSC215_Kotovsky",
        "PRSC215",
        "4069438928"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC310_Petropavlovsk": {
      "name": "PRSC310_Petropavlovsk",
      "aliases": [
        "PRSC310_Petropavlovsk",
        "PRSC310",
        "3969824208"
      ],
      "mainGunCaliberMm": 220,
      "mainGunHePenMm": 37,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50,
            180
          ],
          "bow": [
            50,
            180
          ],
          "stern": [
            50,
            180
          ]
        }
      }
    },
    "PRSC503_Oleg": {
      "name": "PRSC503_Oleg",
      "aliases": [
        "PRSC503_Oleg",
        "PRSC503",
        "3767449040"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25,
            80
          ],
          "stern": [
            25,
            80
          ]
        },
        "deck": {
          "values": [
            11,
            25
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC505_KrasniKrym": {
      "name": "PRSC505_KrasniKrym",
      "aliases": [
        "PRSC505_KrasniKrym",
        "PRSC505",
        "3765351888"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13,
            20
          ],
          "stern": [
            20
          ]
        },
        "deck": {
          "values": [
            20,
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            25
          ],
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        }
      }
    },
    "PRSC506_Molotov_1943": {
      "name": "PRSC506_Molotov_1943",
      "aliases": [
        "PRSC506_Molotov_1943",
        "PRSC506",
        "3764303312"
      ],
      "mainGunCaliberMm": 180,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            18
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC508_Kutuzov_1952": {
      "name": "PRSC508_Kutuzov_1952",
      "aliases": [
        "PRSC508_Kutuzov_1952",
        "PRSC508",
        "3762206160"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC509_Kronshtadt": {
      "name": "PRSC509_Kronshtadt",
      "aliases": [
        "PRSC509_Kronshtadt",
        "PRSC509",
        "3761157584"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27,
            230
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC510_Stalingrad": {
      "name": "PRSC510_Stalingrad",
      "aliases": [
        "PRSC510_Stalingrad",
        "PRSC510",
        "3760109008"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50
          ],
          "bow": [
            50
          ],
          "stern": [
            50
          ]
        }
      }
    },
    "PRSC513_Varyag": {
      "name": "PRSC513_Varyag",
      "aliases": [
        "PRSC513_Varyag",
        "PRSC513",
        "3756963280"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC515_Mikoyan": {
      "name": "PRSC515_Mikoyan",
      "aliases": [
        "PRSC515_Mikoyan",
        "PRSC515",
        "3754866128"
      ],
      "mainGunCaliberMm": 180,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC518_Lazo": {
      "name": "PRSC518_Lazo",
      "aliases": [
        "PRSC518_Lazo",
        "PRSC518",
        "3751720400"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            20
          ],
          "bow": [
            20
          ],
          "stern": []
        }
      }
    },
    "PRSC520_Stalingrad": {
      "name": "PRSC520_Stalingrad",
      "aliases": [
        "PRSC520_Stalingrad",
        "PRSC520",
        "3749623248"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50
          ],
          "bow": [
            50
          ],
          "stern": [
            50
          ]
        }
      }
    },
    "PRSC523_AZUR_Avrora": {
      "name": "PRSC523_AZUR_Avrora",
      "aliases": [
        "PRSC523_AZUR_Avrora",
        "PRSC523",
        "3746477520"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6,
            9
          ]
        },
        "deck": {
          "values": [
            51
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC525_Kirov": {
      "name": "PRSC525_Kirov",
      "aliases": [
        "PRSC525_Kirov",
        "PRSC525",
        "3744380368"
      ],
      "mainGunCaliberMm": 180,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            18
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC528_Ochakov": {
      "name": "PRSC528_Ochakov",
      "aliases": [
        "PRSC528_Ochakov",
        "PRSC528",
        "3741234640"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC530_Black_Smolensk": {
      "name": "PRSC530_Black_Smolensk",
      "aliases": [
        "PRSC530_Black_Smolensk",
        "PRSC530",
        "3739137488"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC538_Petr_Bagration": {
      "name": "PRSC538_Petr_Bagration",
      "aliases": [
        "PRSC538_Petr_Bagration",
        "PRSC538",
        "3730748880"
      ],
      "mainGunCaliberMm": 180,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC548_Bagration": {
      "name": "PRSC548_Bagration",
      "aliases": [
        "PRSC548_Bagration",
        "PRSC548",
        "3720263120"
      ],
      "mainGunCaliberMm": 180,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC558_Dmitry_Pozharsky": {
      "name": "PRSC558_Dmitry_Pozharsky",
      "aliases": [
        "PRSC558_Dmitry_Pozharsky",
        "PRSC558",
        "3709777360"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC568_Black_Lazo": {
      "name": "PRSC568_Black_Lazo",
      "aliases": [
        "PRSC568_Black_Lazo",
        "PRSC568",
        "3699291600"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            20
          ],
          "bow": [
            20
          ],
          "stern": []
        }
      }
    },
    "PRSC606_Admiral_Makarov": {
      "name": "PRSC606_Admiral_Makarov",
      "aliases": [
        "PRSC606_Admiral_Makarov",
        "PRSC606",
        "3659445712"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 38,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            20
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC610_Smolensk": {
      "name": "PRSC610_Smolensk",
      "aliases": [
        "PRSC610_Smolensk",
        "PRSC610",
        "3655251408"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC709_Vyazma": {
      "name": "PRSC709_Vyazma",
      "aliases": [
        "PRSC709_Vyazma",
        "PRSC709",
        "3551442384"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50,
            100
          ],
          "bow": [
            50,
            100
          ],
          "stern": [
            50
          ]
        }
      }
    },
    "PRSC710_Sevastopol": {
      "name": "PRSC710_Sevastopol",
      "aliases": [
        "PRSC710_Sevastopol",
        "PRSC710",
        "3550393808"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 63,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30,
            230
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC719_Kozma_Minin": {
      "name": "PRSC719_Kozma_Minin",
      "aliases": [
        "PRSC719_Kozma_Minin",
        "PRSC719",
        "3540956624"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC810_Komissar": {
      "name": "PRSC810_Komissar",
      "aliases": [
        "PRSC810_Komissar",
        "PRSC810",
        "3445536208"
      ],
      "mainGunCaliberMm": 240,
      "mainGunHePenMm": 40,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            16,
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC818_Cyber_Dmitry_Pozharsky": {
      "name": "PRSC818_Cyber_Dmitry_Pozharsky",
      "aliases": [
        "PRSC818_Cyber_Dmitry_Pozharsky",
        "PRSC818",
        "3437147600"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSC910_Pr_66_Moskva": {
      "name": "PRSC910_Pr_66_Moskva",
      "aliases": [
        "PRSC910_Pr_66_Moskva",
        "PRSC910",
        "3340678608"
      ],
      "mainGunCaliberMm": 220,
      "mainGunHePenMm": 37,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50,
            155
          ],
          "bow": [
            50
          ],
          "stern": [
            50,
            155
          ]
        }
      }
    },
    "PRSC920_PostApoc_Petropavlovsk": {
      "name": "PRSC920_PostApoc_Petropavlovsk",
      "aliases": [
        "PRSC920_PostApoc_Petropavlovsk",
        "PRSC920",
        "3330192848"
      ],
      "mainGunCaliberMm": 220,
      "mainGunHePenMm": 37,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50,
            180
          ],
          "bow": [
            50,
            180
          ],
          "stern": [
            50,
            180
          ]
        }
      }
    },
    "PRSC980_Vladimir_Monomakh": {
      "name": "PRSC980_Vladimir_Monomakh",
      "aliases": [
        "PRSC980_Vladimir_Monomakh",
        "PRSC980",
        "3267278288"
      ],
      "mainGunCaliberMm": 180,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50
          ],
          "bow": [
            50
          ],
          "stern": [
            50
          ]
        }
      }
    },
    "PRSC990_Petrozavodsk": {
      "name": "PRSC990_Petrozavodsk",
      "aliases": [
        "PRSC990_Petrozavodsk",
        "PRSC990",
        "3256792528"
      ],
      "mainGunCaliberMm": 220,
      "mainGunHePenMm": 37,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50,
            180
          ],
          "bow": [
            50,
            180
          ],
          "stern": [
            50,
            180
          ]
        }
      }
    },
    "PRSC999_Seal": {
      "name": "PRSC999_Seal",
      "aliases": [
        "PRSC999_Seal",
        "PRSC999",
        "3247355344"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            88
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD001_Gremyashchy_1942": {
      "name": "PRSD001_Gremyashchy_1942",
      "aliases": [
        "PRSD001_Gremyashchy_1942",
        "PRSD001",
        "4293801424"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            13
          ],
          "stern": [
            10,
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD102_SM_Storojevoy": {
      "name": "PRSD102_SM_Storojevoy",
      "aliases": [
        "PRSD102_SM_Storojevoy",
        "PRSD102",
        "4187895248"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD103_Derzky": {
      "name": "PRSD103_Derzky",
      "aliases": [
        "PRSD103_Derzky",
        "PRSD103",
        "4186846672"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10,
            14
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            12
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD104_Izyaslav": {
      "name": "PRSD104_Izyaslav",
      "aliases": [
        "PRSD104_Izyaslav",
        "PRSD104",
        "4185798096"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10,
            14
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            14,
            15
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD105_Pr_7_Gnevny": {
      "name": "PRSD105_Pr_7_Gnevny",
      "aliases": [
        "PRSD105_Pr_7_Gnevny",
        "PRSD105",
        "4184749520"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            13
          ],
          "stern": [
            10,
            13,
            19
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD106_Pr_30_Ognevoy": {
      "name": "PRSD106_Pr_30_Ognevoy",
      "aliases": [
        "PRSD106_Pr_30_Ognevoy",
        "PRSD106",
        "4183700944"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13,
            16
          ],
          "stern": [
            13,
            16
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD107_Pr_35_Udaloy": {
      "name": "PRSD107_Pr_35_Udaloy",
      "aliases": [
        "PRSD107_Pr_35_Udaloy",
        "PRSD107",
        "4182652368"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD108_Pr_20i_Tashkent": {
      "name": "PRSD108_Pr_20i_Tashkent",
      "aliases": [
        "PRSD108_Pr_20i_Tashkent",
        "PRSD108",
        "4181603792"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD109_Pr_48_Kiev": {
      "name": "PRSD109_Pr_48_Kiev",
      "aliases": [
        "PRSD109_Pr_48_Kiev",
        "PRSD109",
        "4180555216"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16,
            19
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD110_Pr_24_Khabarovsk": {
      "name": "PRSD110_Pr_24_Khabarovsk",
      "aliases": [
        "PRSD110_Pr_24_Khabarovsk",
        "PRSD110",
        "4179506640"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            25,
            50
          ],
          "stern": [
            19,
            25,
            50
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD111_Zorky": {
      "name": "PRSD111_Zorky",
      "aliases": [
        "PRSD111_Zorky",
        "PRSD111",
        "4178458064"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            25,
            50
          ],
          "stern": [
            19,
            25,
            50
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD205_Podvoisky_pr_1929": {
      "name": "PRSD205_Podvoisky_pr_1929",
      "aliases": [
        "PRSD205_Podvoisky_pr_1929",
        "PRSD205",
        "4079891920"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            13
          ],
          "stern": [
            10,
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD206_Pr_7": {
      "name": "PRSD206_Pr_7",
      "aliases": [
        "PRSD206_Pr_7",
        "PRSD206",
        "4078843344"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16,
            19
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD207_Minsk": {
      "name": "PRSD207_Minsk",
      "aliases": [
        "PRSD207_Minsk",
        "PRSD207",
        "4077794768"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD208_Pr_30": {
      "name": "PRSD208_Pr_30",
      "aliases": [
        "PRSD208_Pr_30",
        "PRSD208",
        "4076746192"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD210_Grozovoy_pr_40N": {
      "name": "PRSD210_Grozovoy_pr_40N",
      "aliases": [
        "PRSD210_Grozovoy_pr_40N",
        "PRSD210",
        "4074649040"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD308_Pr_48": {
      "name": "PRSD308_Pr_48",
      "aliases": [
        "PRSD308_Pr_48",
        "PRSD308",
        "3971888592"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD409_Pr_20i_Tashkent": {
      "name": "PRSD409_Pr_20i_Tashkent",
      "aliases": [
        "PRSD409_Pr_20i_Tashkent",
        "PRSD409",
        "3865982416"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD410_Delny": {
      "name": "PRSD410_Delny",
      "aliases": [
        "PRSD410_Delny",
        "PRSD410",
        "3864933840"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD505_Okhotnik_1917": {
      "name": "PRSD505_Okhotnik_1917",
      "aliases": [
        "PRSD505_Okhotnik_1917",
        "PRSD505",
        "3765319120"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            13
          ],
          "stern": [
            10,
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD507_Leningrad_1944": {
      "name": "PRSD507_Leningrad_1944",
      "aliases": [
        "PRSD507_Leningrad_1944",
        "PRSD507",
        "3763221968"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD517_Tashkent_1939": {
      "name": "PRSD517_Tashkent_1939",
      "aliases": [
        "PRSD517_Tashkent_1939",
        "PRSD517",
        "3752736208"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD709_Pr_41_Neustrashimy": {
      "name": "PRSD709_Pr_41_Neustrashimy",
      "aliases": [
        "PRSD709_Pr_41_Neustrashimy",
        "PRSD709",
        "3551409616"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD718_Provorny": {
      "name": "PRSD718_Provorny",
      "aliases": [
        "PRSD718_Provorny",
        "PRSD718",
        "3541972432"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            25
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD810_R_10": {
      "name": "PRSD810_R_10",
      "aliases": [
        "PRSD810_R_10",
        "PRSD810",
        "3445503440"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD909_Black_Neustrashimy": {
      "name": "PRSD909_Black_Neustrashimy",
      "aliases": [
        "PRSD909_Black_Neustrashimy",
        "PRSD909",
        "3341694416"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD910_Grozovoy_pr_40N": {
      "name": "PRSD910_Grozovoy_pr_40N",
      "aliases": [
        "PRSD910_Grozovoy_pr_40N",
        "PRSD910",
        "3340645840"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSD919_Azur_Tashkent": {
      "name": "PRSD919_Azur_Tashkent",
      "aliases": [
        "PRSD919_Azur_Tashkent",
        "PRSD919",
        "3331208656"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSS106_S_1": {
      "name": "PRSS106_S_1",
      "aliases": [
        "PRSS106_S_1",
        "PRSS106",
        "4183209424"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 29,
      "armor": {
        "bowStern": {
          "bow": [
            13,
            16,
            19
          ],
          "stern": [
            13,
            16,
            19
          ]
        },
        "deck": {
          "values": [
            13,
            16,
            19
          ]
        },
        "side": {
          "values": [
            13,
            16,
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSS108_L20": {
      "name": "PRSS108_L20",
      "aliases": [
        "PRSS108_L20",
        "PRSS108",
        "4181112272"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 29,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSS110_K_type": {
      "name": "PRSS110_K_type",
      "aliases": [
        "PRSS110_K_type",
        "PRSS110",
        "4179015120"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 29,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSS508_S_189": {
      "name": "PRSS508_S_189",
      "aliases": [
        "PRSS508_S_189",
        "PRSS508",
        "3761681872"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PRSS999_Tst_sub": {
      "name": "PRSS999_Tst_sub",
      "aliases": [
        "PRSS999_Tst_sub",
        "PRSS999",
        "3246831056"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            13,
            16
          ],
          "stern": [
            10,
            13,
            16
          ]
        },
        "deck": {
          "values": [
            10,
            13,
            16
          ]
        },
        "side": {
          "values": [
            10,
            13,
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PSSB719_Victoria": {
      "name": "PSSB719_Victoria",
      "aliases": [
        "PSSB719_Victoria",
        "PSSB719",
        "3540989360"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            70
          ],
          "stern": [
            13,
            32
          ]
        },
        "deck": {
          "values": [
            45
          ]
        },
        "side": {
          "values": [
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            130
          ],
          "bow": [
            130
          ],
          "stern": []
        }
      }
    },
    "PSSC101_Jupiter": {
      "name": "PSSC101_Jupiter",
      "aliases": [
        "PSSC101_Jupiter",
        "PSSC101",
        "4188976560"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PSSC102_Mendez_Nunez": {
      "name": "PSSC102_Mendez_Nunez",
      "aliases": [
        "PSSC102_Mendez_Nunez",
        "PSSC102",
        "4187927984"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            38,
            50,
            75
          ],
          "bow": [
            38,
            50,
            75
          ],
          "stern": [
            50,
            75
          ]
        }
      }
    },
    "PSSC103_Navarra": {
      "name": "PSSC103_Navarra",
      "aliases": [
        "PSSC103_Navarra",
        "PSSC103",
        "4186879408"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            76
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            57,
            69
          ],
          "bow": [
            69
          ],
          "stern": [
            57
          ]
        }
      }
    },
    "PSSC104_Almirante_Cervera": {
      "name": "PSSC104_Almirante_Cervera",
      "aliases": [
        "PSSC104_Almirante_Cervera",
        "PSSC104",
        "4185830832"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            38,
            57,
            76
          ],
          "bow": [
            38,
            57,
            76
          ],
          "stern": [
            57,
            76
          ]
        }
      }
    },
    "PSSC105_Galicia": {
      "name": "PSSC105_Galicia",
      "aliases": [
        "PSSC105_Galicia",
        "PSSC105",
        "4184782256"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            38,
            57,
            76
          ],
          "bow": [
            38,
            57,
            76
          ],
          "stern": [
            57,
            76
          ]
        }
      }
    },
    "PSSC106_Baleares": {
      "name": "PSSC106_Baleares",
      "aliases": [
        "PSSC106_Baleares",
        "PSSC106",
        "4183733680"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PSSC107_Asturias": {
      "name": "PSSC107_Asturias",
      "aliases": [
        "PSSC107_Asturias",
        "PSSC107",
        "4182685104"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PSSC108_Cataluna": {
      "name": "PSSC108_Cataluna",
      "aliases": [
        "PSSC108_Cataluna",
        "PSSC108",
        "4181636528"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PSSC109_Andalucia": {
      "name": "PSSC109_Andalucia",
      "aliases": [
        "PSSC109_Andalucia",
        "PSSC109",
        "4180587952"
      ],
      "mainGunCaliberMm": 234,
      "mainGunHePenMm": 39,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27,
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PSSC110_Castilla": {
      "name": "PSSC110_Castilla",
      "aliases": [
        "PSSC110_Castilla",
        "PSSC110",
        "4179539376"
      ],
      "mainGunCaliberMm": 254,
      "mainGunHePenMm": 42,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PSSC506_Canarias": {
      "name": "PSSC506_Canarias",
      "aliases": [
        "PSSC506_Canarias",
        "PSSC506",
        "3764303280"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PSSC508_Numancia": {
      "name": "PSSC508_Numancia",
      "aliases": [
        "PSSC508_Numancia",
        "PSSC508",
        "3762206128"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PSSC719_Almirante_Oquendo": {
      "name": "PSSC719_Almirante_Oquendo",
      "aliases": [
        "PSSC719_Almirante_Oquendo",
        "PSSC719",
        "3540956592"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27,
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PSSD510_Alvaro_de_Bazan": {
      "name": "PSSD510_Alvaro_de_Bazan",
      "aliases": [
        "PSSD510_Alvaro_de_Bazan",
        "PSSD510",
        "3760076208"
      ],
      "mainGunCaliberMm": 135,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSB507_Yukon": {
      "name": "PUSB507_Yukon",
      "aliases": [
        "PUSB507_Yukon",
        "PUSB507",
        "3763287408"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26,
            356,
            381
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSB710_Irresistible": {
      "name": "PUSB710_Irresistible",
      "aliases": [
        "PUSB710_Irresistible",
        "PUSB710",
        "3550426480"
      ],
      "mainGunCaliberMm": 234,
      "mainGunHePenMm": 39,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC001_Sutlej": {
      "name": "PUSC001_Sutlej",
      "aliases": [
        "PUSC001_Sutlej",
        "PUSC001",
        "4293834096"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10,
            13
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC010_Cerberus": {
      "name": "PUSC010_Cerberus",
      "aliases": [
        "PUSC010_Cerberus",
        "PUSC010",
        "4284396912"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            32,
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC012_Port_Jackson": {
      "name": "PUSC012_Port_Jackson",
      "aliases": [
        "PUSC012_Port_Jackson",
        "PUSC012",
        "4282299760"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC013_Caradoc": {
      "name": "PUSC013_Caradoc",
      "aliases": [
        "PUSC013_Caradoc",
        "PUSC013",
        "4281251184"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            38,
            57,
            76
          ],
          "bow": [
            38,
            57,
            76
          ],
          "stern": [
            57,
            76
          ]
        }
      }
    },
    "PUSC014_Dunedin": {
      "name": "PUSC014_Dunedin",
      "aliases": [
        "PUSC014_Dunedin",
        "PUSC014",
        "4280202608"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            38,
            57,
            76
          ],
          "bow": [
            38,
            57,
            76
          ],
          "stern": [
            57,
            76
          ]
        }
      }
    },
    "PUSC015_Delhi": {
      "name": "PUSC015_Delhi",
      "aliases": [
        "PUSC015_Delhi",
        "PUSC015",
        "4279154032"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC016_Hobart": {
      "name": "PUSC016_Hobart",
      "aliases": [
        "PUSC016_Hobart",
        "PUSC016",
        "4278105456"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25,
            32
          ]
        },
        "side": {
          "values": [
            16,
            100
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC017_Uganda": {
      "name": "PUSC017_Uganda",
      "aliases": [
        "PUSC017_Uganda",
        "PUSC017",
        "4277056880"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16,
            38
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC018_Auckland": {
      "name": "PUSC018_Auckland",
      "aliases": [
        "PUSC018_Auckland",
        "PUSC018",
        "4276008304"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25,
            76
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC019_Encounter": {
      "name": "PUSC019_Encounter",
      "aliases": [
        "PUSC019_Encounter",
        "PUSC019",
        "4274959728"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC506_Perth_1942": {
      "name": "PUSC506_Perth_1942",
      "aliases": [
        "PUSC506_Perth_1942",
        "PUSC506",
        "3764303216"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25,
            32
          ]
        },
        "side": {
          "values": [
            16,
            100
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC509_Hector": {
      "name": "PUSC509_Hector",
      "aliases": [
        "PUSC509_Hector",
        "PUSC509",
        "3761157488"
      ],
      "mainGunCaliberMm": 133,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25,
            114
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC510_Brisbane": {
      "name": "PUSC510_Brisbane",
      "aliases": [
        "PUSC510_Brisbane",
        "PUSC510",
        "3760108912"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC516_Mysore": {
      "name": "PUSC516_Mysore",
      "aliases": [
        "PUSC516_Mysore",
        "PUSC516",
        "3753817456"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC710_Pioneer": {
      "name": "PUSC710_Pioneer",
      "aliases": [
        "PUSC710_Pioneer",
        "PUSC710",
        "3550393712"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC717_Gambia": {
      "name": "PUSC717_Gambia",
      "aliases": [
        "PUSC717_Gambia",
        "PUSC717",
        "3543053680"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16,
            38
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC810_Black_Brisbane": {
      "name": "PUSC810_Black_Brisbane",
      "aliases": [
        "PUSC810_Black_Brisbane",
        "PUSC810",
        "3445536112"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSC997_Gambra": {
      "name": "PUSC997_Gambra",
      "aliases": [
        "PUSC997_Gambra",
        "PUSC997",
        "3249452400"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSD503_Vampire": {
      "name": "PUSD503_Vampire",
      "aliases": [
        "PUSD503_Vampire",
        "PUSD503",
        "3767416176"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSD507_Haida": {
      "name": "PUSD507_Haida",
      "aliases": [
        "PUSD507_Haida",
        "PUSD507",
        "3763221872"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19
          ],
          "stern": [
            16,
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSD510_Vampire_2": {
      "name": "PUSD510_Vampire_2",
      "aliases": [
        "PUSD510_Vampire_2",
        "PUSD510",
        "3760076144"
      ],
      "mainGunCaliberMm": 113,
      "mainGunHePenMm": 19,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PUSD517_Huron": {
      "name": "PUSD517_Huron",
      "aliases": [
        "PUSD517_Huron",
        "PUSD517",
        "3752736112"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19
          ],
          "stern": [
            16,
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSA710_Independencia": {
      "name": "PVSA710_Independencia",
      "aliases": [
        "PVSA710_Independencia",
        "PVSA710",
        "3550459216"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            30
          ],
          "stern": [
            19,
            30
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            19,
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSB010_Libertad": {
      "name": "PVSB010_Libertad",
      "aliases": [
        "PVSB010_Libertad",
        "PVSB010",
        "4284429648"
      ],
      "mainGunCaliberMm": 419,
      "mainGunHePenMm": 70,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            51
          ]
        },
        "side": {
          "values": [
            51
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSB018_Ipiranga": {
      "name": "PVSB018_Ipiranga",
      "aliases": [
        "PVSB018_Ipiranga",
        "PVSB018",
        "4276041040"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            51
          ]
        },
        "side": {
          "values": [
            51,
            305
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSB019_Los_Andes": {
      "name": "PVSB019_Los_Andes",
      "aliases": [
        "PVSB019_Los_Andes",
        "PVSB019",
        "4274992464"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            51
          ]
        },
        "side": {
          "values": [
            51,
            330
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSB505_Rio_de_Janeiro": {
      "name": "PVSB505_Rio_de_Janeiro",
      "aliases": [
        "PVSB505_Rio_de_Janeiro",
        "PVSB505",
        "3765384528"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            38
          ],
          "stern": [
            19,
            38
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            152,
            229
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            102
          ],
          "bow": [
            102
          ],
          "stern": [
            102
          ]
        }
      }
    },
    "PVSB508_Atlantico": {
      "name": "PVSB508_Atlantico",
      "aliases": [
        "PVSB508_Atlantico",
        "PVSB508",
        "3762238800"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            51
          ]
        },
        "side": {
          "values": [
            152
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSB710_Sete_de_Setembro": {
      "name": "PVSB710_Sete_de_Setembro",
      "aliases": [
        "PVSB710_Sete_de_Setembro",
        "PVSB710",
        "3550426448"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSB719_Valparaiso": {
      "name": "PVSB719_Valparaiso",
      "aliases": [
        "PVSB719_Valparaiso",
        "PVSB719",
        "3540989264"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            40,
            343,
            356
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSB990_Comodoro": {
      "name": "PVSB990_Comodoro",
      "aliases": [
        "PVSB990_Comodoro",
        "PVSB990",
        "3256825168"
      ],
      "mainGunCaliberMm": 419,
      "mainGunHePenMm": 70,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            51
          ]
        },
        "side": {
          "values": [
            51
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSB999_Cordillera": {
      "name": "PVSB999_Cordillera",
      "aliases": [
        "PVSB999_Cordillera",
        "PVSB999",
        "3247387984"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            51
          ]
        },
        "side": {
          "values": [
            51
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSC101_Hercules": {
      "name": "PVSC101_Hercules",
      "aliases": [
        "PVSC101_Hercules",
        "PVSC101",
        "4188976464"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSC102_Almirante_Barroso": {
      "name": "PVSC102_Almirante_Barroso",
      "aliases": [
        "PVSC102_Almirante_Barroso",
        "PVSC102",
        "4187927888"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSC103_Vicente_Guerrero": {
      "name": "PVSC103_Vicente_Guerrero",
      "aliases": [
        "PVSC103_Vicente_Guerrero",
        "PVSC103",
        "4186879312"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            76
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            57,
            69
          ],
          "bow": [
            69
          ],
          "stern": [
            57
          ]
        }
      }
    },
    "PVSC104_Cordoba": {
      "name": "PVSC104_Cordoba",
      "aliases": [
        "PVSC104_Cordoba",
        "PVSC104",
        "4185830736"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            38,
            57,
            76
          ],
          "bow": [
            38,
            57,
            76
          ],
          "stern": [
            57,
            76
          ]
        }
      }
    },
    "PVSC105_La_Argentina": {
      "name": "PVSC105_La_Argentina",
      "aliases": [
        "PVSC105_La_Argentina",
        "PVSC105",
        "4184782160"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13,
            38
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSC106_Almirante_Cochrane": {
      "name": "PVSC106_Almirante_Cochrane",
      "aliases": [
        "PVSC106_Almirante_Cochrane",
        "PVSC106",
        "4183733584"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            20,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            30
          ],
          "bow": [
            30
          ],
          "stern": []
        }
      }
    },
    "PVSC107_Coronel_Bolognesi": {
      "name": "PVSC107_Coronel_Bolognesi",
      "aliases": [
        "PVSC107_Coronel_Bolognesi",
        "PVSC107",
        "4182685008"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16,
            38
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSC108_Ignacio_Allende": {
      "name": "PVSC108_Ignacio_Allende",
      "aliases": [
        "PVSC108_Ignacio_Allende",
        "PVSC108",
        "4181636432"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSC109_Santander": {
      "name": "PVSC109_Santander",
      "aliases": [
        "PVSC109_Santander",
        "PVSC109",
        "4180587856"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSC110_San_Martin": {
      "name": "PVSC110_San_Martin",
      "aliases": [
        "PVSC110_San_Martin",
        "PVSC110",
        "4179539280"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSC502_Almirante_Abreu": {
      "name": "PVSC502_Almirante_Abreu",
      "aliases": [
        "PVSC502_Almirante_Abreu",
        "PVSC502",
        "3768497488"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSC507_Nueve_de_Julio_1951": {
      "name": "PVSC507_Nueve_de_Julio_1951",
      "aliases": [
        "PVSC507_Nueve_de_Julio_1951",
        "PVSC507",
        "3763254608"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSC508_Almirante_Grau": {
      "name": "PVSC508_Almirante_Grau",
      "aliases": [
        "PVSC508_Almirante_Grau",
        "PVSC508",
        "3762206032"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSC708_Comandante_Aguirre": {
      "name": "PVSC708_Comandante_Aguirre",
      "aliases": [
        "PVSC708_Comandante_Aguirre",
        "PVSC708",
        "3552490832"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50
          ],
          "bow": [
            50
          ],
          "stern": [
            50
          ]
        }
      }
    },
    "PVSD506_Jurua": {
      "name": "PVSD506_Jurua",
      "aliases": [
        "PVSD506_Jurua",
        "PVSD506",
        "3764270416"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PVSD710_La_Pampa": {
      "name": "PVSD710_La_Pampa",
      "aliases": [
        "PVSD710_La_Pampa",
        "PVSD710",
        "3550360912"
      ],
      "mainGunCaliberMm": 113,
      "mainGunHePenMm": 19,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSB010_Thor": {
      "name": "PWSB010_Thor",
      "aliases": [
        "PWSB010_Thor",
        "PWSB010",
        "4284429616"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PWSB014_Yavuz_Sultan_Selim": {
      "name": "PWSB014_Yavuz_Sultan_Selim",
      "aliases": [
        "PWSB014_Yavuz_Sultan_Selim",
        "PWSB014",
        "4280235312"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 47,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19,
            25,
            35
          ]
        },
        "side": {
          "values": [
            150,
            200
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            80,
            100,
            120
          ],
          "bow": [
            80,
            100,
            120
          ],
          "stern": [
            100
          ]
        }
      }
    },
    "PWSB015_Tegetthoff": {
      "name": "PWSB015_Tegetthoff",
      "aliases": [
        "PWSB015_Tegetthoff",
        "PWSB015",
        "4279186736"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            30
          ],
          "stern": [
            19,
            30
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            180
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            110,
            130,
            150,
            180,
            280
          ],
          "bow": [
            110,
            130,
            150,
            180,
            280
          ],
          "stern": [
            180,
            280
          ]
        }
      }
    },
    "PWSB016_Laudon": {
      "name": "PWSB016_Laudon",
      "aliases": [
        "PWSB016_Laudon",
        "PWSB016",
        "4278138160"
      ],
      "mainGunCaliberMm": 350,
      "mainGunHePenMm": 58,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            36
          ]
        },
        "side": {
          "values": [
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40,
            200
          ],
          "bow": [
            40
          ],
          "stern": [
            200
          ]
        }
      }
    },
    "PWSB017_Chios": {
      "name": "PWSB017_Chios",
      "aliases": [
        "PWSB017_Chios",
        "PWSB017",
        "4277089584"
      ],
      "mainGunCaliberMm": 350,
      "mainGunHePenMm": 58.3,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            30,
            120
          ],
          "bow": [
            30,
            120
          ],
          "stern": []
        }
      }
    },
    "PWSB018_Enigheten": {
      "name": "PWSB018_Enigheten",
      "aliases": [
        "PWSB018_Enigheten",
        "PWSB018",
        "4276041008"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            40
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSB019_Gustav_den_Store": {
      "name": "PWSB019_Gustav_den_Store",
      "aliases": [
        "PWSB019_Gustav_den_Store",
        "PWSB019",
        "4274992432"
      ],
      "mainGunCaliberMm": 381,
      "mainGunHePenMm": 64,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSB504_Viribus_Unitis": {
      "name": "PWSB504_Viribus_Unitis",
      "aliases": [
        "PWSB504_Viribus_Unitis",
        "PWSB504",
        "3766433072"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            30
          ],
          "stern": [
            19,
            30
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            180
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            110,
            130,
            150,
            180,
            280
          ],
          "bow": [
            110,
            130,
            150,
            180,
            280
          ],
          "stern": [
            180,
            280
          ]
        }
      }
    },
    "PWSB509_Karl_XIV_Johan": {
      "name": "PWSB509_Karl_XIV_Johan",
      "aliases": [
        "PWSB509_Karl_XIV_Johan",
        "PWSB509",
        "3761190192"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            150,
            220
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            35,
            95
          ],
          "bow": [
            35
          ],
          "stern": [
            95
          ]
        }
      }
    },
    "PWSB707_Lugdunum": {
      "name": "PWSB707_Lugdunum",
      "aliases": [
        "PWSB707_Lugdunum",
        "PWSB707",
        "3553572144"
      ],
      "mainGunCaliberMm": 340,
      "mainGunHePenMm": 57,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            12,
            26
          ],
          "stern": [
            26,
            30
          ]
        },
        "deck": {
          "values": [
            26,
            30
          ]
        },
        "side": {
          "values": [
            180
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            120,
            180
          ],
          "bow": [
            180
          ],
          "stern": [
            120
          ]
        }
      }
    },
    "PWSB718_Turgut_Reis": {
      "name": "PWSB718_Turgut_Reis",
      "aliases": [
        "PWSB718_Turgut_Reis",
        "PWSB718",
        "3542037808"
      ],
      "mainGunCaliberMm": 419,
      "mainGunHePenMm": 70,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            305
          ],
          "bow": [
            305
          ],
          "stern": [
            305
          ]
        }
      }
    },
    "PWSB719_Niord": {
      "name": "PWSB719_Niord",
      "aliases": [
        "PWSB719_Niord",
        "PWSB719",
        "3540989232"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            18,
            32
          ],
          "stern": [
            20,
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            150
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSB909_Black_Karl_XIV_Johan": {
      "name": "PWSB909_Black_Karl_XIV_Johan",
      "aliases": [
        "PWSB909_Black_Karl_XIV_Johan",
        "PWSB909",
        "3341759792"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            150,
            220
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            35,
            95
          ],
          "bow": [
            35
          ],
          "stern": [
            95
          ]
        }
      }
    },
    "PWSC101_Gryf": {
      "name": "PWSC101_Gryf",
      "aliases": [
        "PWSC101_Gryf",
        "PWSC101",
        "4188976432"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSC506_Elli": {
      "name": "PWSC506_Elli",
      "aliases": [
        "PWSC506_Elli",
        "PWSC506",
        "3764303152"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            30
          ],
          "stern": [
            16,
            30
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            20,
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSC710_Svea": {
      "name": "PWSC710_Svea",
      "aliases": [
        "PWSC710_Svea",
        "PWSC710",
        "3550393648"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            25,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSC718_Regele_Carol_I": {
      "name": "PWSC718_Regele_Carol_I",
      "aliases": [
        "PWSC718_Regele_Carol_I",
        "PWSC718",
        "3542005040"
      ],
      "mainGunCaliberMm": 280,
      "mainGunHePenMm": 47,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25,
            45
          ]
        },
        "deck": {
          "values": [
            28
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD102_Tatra": {
      "name": "PWSD102_Tatra",
      "aliases": [
        "PWSD102_Tatra",
        "PWSD102",
        "4187895088"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD103_Romulus": {
      "name": "PWSD103_Romulus",
      "aliases": [
        "PWSD103_Romulus",
        "PWSD103",
        "4186846512"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD104_Klas_Horn": {
      "name": "PWSD104_Klas_Horn",
      "aliases": [
        "PWSD104_Klas_Horn",
        "PWSD104",
        "4185797936"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD105_Visby": {
      "name": "PWSD105_Visby",
      "aliases": [
        "PWSD105_Visby",
        "PWSD105",
        "4184749360"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD106_Vasteras": {
      "name": "PWSD106_Vasteras",
      "aliases": [
        "PWSD106_Vasteras",
        "PWSD106",
        "4183700784"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD107_Skane": {
      "name": "PWSD107_Skane",
      "aliases": [
        "PWSD107_Skane",
        "PWSD107",
        "4182652208"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD108_Oland": {
      "name": "PWSD108_Oland",
      "aliases": [
        "PWSD108_Oland",
        "PWSD108",
        "4181603632"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD109_Ostergotland": {
      "name": "PWSD109_Ostergotland",
      "aliases": [
        "PWSD109_Ostergotland",
        "PWSD109",
        "4180555056"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD110_Halland": {
      "name": "PWSD110_Halland",
      "aliases": [
        "PWSD110_Halland",
        "PWSD110",
        "4179506480"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD111_Dalarna": {
      "name": "PWSD111_Dalarna",
      "aliases": [
        "PWSD111_Dalarna",
        "PWSD111",
        "4178457904"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD205_Muavenet": {
      "name": "PWSD205_Muavenet",
      "aliases": [
        "PWSD205_Muavenet",
        "PWSD205",
        "4079891760"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD206_Stord": {
      "name": "PWSD206_Stord",
      "aliases": [
        "PWSD206_Stord",
        "PWSD206",
        "4078843184"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD207_Grom": {
      "name": "PWSD207_Grom",
      "aliases": [
        "PWSD207_Grom",
        "PWSD207",
        "4077794608"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD208_Split": {
      "name": "PWSD208_Split",
      "aliases": [
        "PWSD208_Split",
        "PWSD208",
        "4076746032"
      ],
      "mainGunCaliberMm": 140,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD209_Lambros_Katsonis": {
      "name": "PWSD209_Lambros_Katsonis",
      "aliases": [
        "PWSD209_Lambros_Katsonis",
        "PWSD209",
        "4075697456"
      ],
      "mainGunCaliberMm": 140,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD210_Gdansk": {
      "name": "PWSD210_Gdansk",
      "aliases": [
        "PWSD210_Gdansk",
        "PWSD210",
        "4074648880"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD501_Blyskawica": {
      "name": "PWSD501_Blyskawica",
      "aliases": [
        "PWSD501_Blyskawica",
        "PWSD501",
        "3769513264"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD508_Orkan": {
      "name": "PWSD508_Orkan",
      "aliases": [
        "PWSD508_Orkan",
        "PWSD508",
        "3762173232"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD509_Velos": {
      "name": "PWSD509_Velos",
      "aliases": [
        "PWSD509_Velos",
        "PWSD509",
        "3761124656"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD510_Friesland": {
      "name": "PWSD510_Friesland",
      "aliases": [
        "PWSD510_Friesland",
        "PWSD510",
        "3760076080"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD519_Jager": {
      "name": "PWSD519_Jager",
      "aliases": [
        "PWSD519_Jager",
        "PWSD519",
        "3750638896"
      ],
      "mainGunCaliberMm": 150,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD610_Smaland": {
      "name": "PWSD610_Smaland",
      "aliases": [
        "PWSD610_Smaland",
        "PWSD610",
        "3655218480"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD705_Kalmar": {
      "name": "PWSD705_Kalmar",
      "aliases": [
        "PWSD705_Kalmar",
        "PWSD705",
        "3555603760"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD708_Blyskawica_1944": {
      "name": "PWSD708_Blyskawica_1944",
      "aliases": [
        "PWSD708_Blyskawica_1944",
        "PWSD708",
        "3552458032"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD710_Ragnar": {
      "name": "PWSD710_Ragnar",
      "aliases": [
        "PWSD710_Ragnar",
        "PWSD710",
        "3550360880"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD717_Stord_1943": {
      "name": "PWSD717_Stord_1943",
      "aliases": [
        "PWSD717_Stord_1943",
        "PWSD717",
        "3543020848"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD719_Blyskawica_1952": {
      "name": "PWSD719_Blyskawica_1952",
      "aliases": [
        "PWSD719_Blyskawica_1952",
        "PWSD719",
        "3540923696"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD907_Pirate_Grom": {
      "name": "PWSD907_Pirate_Grom",
      "aliases": [
        "PWSD907_Pirate_Grom",
        "PWSD907",
        "3343791408"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD910_Lappland": {
      "name": "PWSD910_Lappland",
      "aliases": [
        "PWSD910_Lappland",
        "PWSD910",
        "3340645680"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD920_PostApoc_Smaland": {
      "name": "PWSD920_PostApoc_Smaland",
      "aliases": [
        "PWSD920_PostApoc_Smaland",
        "PWSD920",
        "3330159920"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PWSD990_Sodermanland": {
      "name": "PWSD990_Sodermanland",
      "aliases": [
        "PWSD990_Sodermanland",
        "PWSD990",
        "3256759600"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSA001_Invisible_Air_Enemy_1": {
      "name": "PXSA001_Invisible_Air_Enemy_1",
      "aliases": [
        "PXSA001_Invisible_Air_Enemy_1",
        "PXSA001",
        "4293899536"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": []
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSA002_Invisible_Air_Ally_1": {
      "name": "PXSA002_Invisible_Air_Ally_1",
      "aliases": [
        "PXSA002_Invisible_Air_Ally_1",
        "PXSA002",
        "4292850960"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": []
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSA003_Lexington_1944_H2017": {
      "name": "PXSA003_Lexington_1944_H2017",
      "aliases": [
        "PXSA003_Lexington_1944_H2017",
        "PXSA003",
        "4291802384"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13,
            21,
            25
          ],
          "stern": [
            13,
            21
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSA004_Zuikaku_1944_H2017": {
      "name": "PXSA004_Zuikaku_1944_H2017",
      "aliases": [
        "PXSA004_Zuikaku_1944_H2017",
        "PXSA004",
        "4290753808"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            215
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSA005_Hellcarrier": {
      "name": "PXSA005_Hellcarrier",
      "aliases": [
        "PXSA005_Hellcarrier",
        "PXSA005",
        "4289705232"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            95
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSA008_Starfleet_Enterprise": {
      "name": "PXSA008_Starfleet_Enterprise",
      "aliases": [
        "PXSA008_Starfleet_Enterprise",
        "PXSA008",
        "4286559504"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            21
          ],
          "stern": [
            21,
            28
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSA010_Midway_modern": {
      "name": "PXSA010_Midway_modern",
      "aliases": [
        "PXSA010_Midway_modern",
        "PXSA010",
        "4284462352"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            40
          ],
          "stern": [
            19,
            40
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSA807_Ranger": {
      "name": "PXSA807_Ranger",
      "aliases": [
        "PXSA807_Ranger",
        "PXSA807",
        "3448747280"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB001_Mr_Hyde": {
      "name": "PXSB001_Mr_Hyde",
      "aliases": [
        "PXSB001_Mr_Hyde",
        "PXSB001",
        "4293866768"
      ],
      "mainGunCaliberMm": 283,
      "mainGunHePenMm": 100,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            160,
            210,
            240
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            80,
            90,
            100
          ],
          "bow": [
            80,
            100
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PXSB002_Rasputin": {
      "name": "PXSB002_Rasputin",
      "aliases": [
        "PXSB002_Rasputin",
        "PXSB002",
        "4292818192"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            35
          ]
        },
        "side": {
          "values": [
            75
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            100,
            200
          ],
          "bow": [
            100,
            200
          ],
          "stern": []
        }
      }
    },
    "PXSB003_Zeekasa": {
      "name": "PXSB003_Zeekasa",
      "aliases": [
        "PXSB003_Zeekasa",
        "PXSB003",
        "4291769616"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            152,
            229
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            102,
            127,
            178
          ],
          "bow": [
            102,
            127,
            178
          ],
          "stern": [
            102,
            127,
            178
          ]
        }
      }
    },
    "PXSB004_Tirpiz_1942_H2017": {
      "name": "PXSB004_Tirpiz_1942_H2017",
      "aliases": [
        "PXSB004_Tirpiz_1942_H2017",
        "PXSB004",
        "4290721040"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            160
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60
          ],
          "bow": [
            60
          ],
          "stern": []
        }
      }
    },
    "PXSB005_Bismarck_H2017": {
      "name": "PXSB005_Bismarck_H2017",
      "aliases": [
        "PXSB005_Bismarck_H2017",
        "PXSB005",
        "4289672464"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 95,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            160
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB006_Paris": {
      "name": "PXSB006_Paris",
      "aliases": [
        "PXSB006_Paris",
        "PXSB006",
        "4288623888"
      ],
      "mainGunCaliberMm": 431,
      "mainGunHePenMm": 72,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB007_Alldestroyer": {
      "name": "PXSB007_Alldestroyer",
      "aliases": [
        "PXSB007_Alldestroyer",
        "PXSB007",
        "4287575312"
      ],
      "mainGunCaliberMm": 420,
      "mainGunHePenMm": 105,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            150,
            280
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            60,
            120
          ],
          "bow": [
            60,
            120
          ],
          "stern": [
            120
          ]
        }
      }
    },
    "PXSB008_North_Carolina_H2018": {
      "name": "PXSB008_North_Carolina_H2018",
      "aliases": [
        "PXSB008_North_Carolina_H2018",
        "PXSB008",
        "4286526736"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB009_Yamato_H2019": {
      "name": "PXSB009_Yamato_H2019",
      "aliases": [
        "PXSB009_Yamato_H2019",
        "PXSB009",
        "4285478160"
      ],
      "mainGunCaliberMm": 460,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32,
            50
          ],
          "stern": [
            32,
            50
          ]
        },
        "deck": {
          "values": [
            57
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB010_France_H2019": {
      "name": "PXSB010_France_H2019",
      "aliases": [
        "PXSB010_France_H2019",
        "PXSB010",
        "4284429584"
      ],
      "mainGunCaliberMm": 431,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB011_Montana_H2019": {
      "name": "PXSB011_Montana_H2019",
      "aliases": [
        "PXSB011_Montana_H2019",
        "PXSB011",
        "4283381008"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB015_Crab_Battleship": {
      "name": "PXSB015_Crab_Battleship",
      "aliases": [
        "PXSB015_Crab_Battleship",
        "PXSB015",
        "4279186704"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 201,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            50
          ],
          "stern": []
        },
        "deck": {
          "values": []
        },
        "side": {
          "values": [
            50,
            200
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            400
          ],
          "bow": [
            400
          ],
          "stern": []
        }
      }
    },
    "PXSB016_France_Borg_V1": {
      "name": "PXSB016_France_Borg_V1",
      "aliases": [
        "PXSB016_France_Borg_V1",
        "PXSB016",
        "4278138128"
      ],
      "mainGunCaliberMm": 431,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            30
          ],
          "stern": [
            30
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            100,
            120
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB017_France_Borg_V2": {
      "name": "PXSB017_France_Borg_V2",
      "aliases": [
        "PXSB017_France_Borg_V2",
        "PXSB017",
        "4277089552"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            30
          ],
          "stern": [
            30
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            100,
            120
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB027_Gneisenau_Vulkans": {
      "name": "PXSB027_Gneisenau_Vulkans",
      "aliases": [
        "PXSB027_Gneisenau_Vulkans",
        "PXSB027",
        "4266603792"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            45
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            70,
            90
          ],
          "bow": [
            70
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PXSB030_Yamato_BorgBoss": {
      "name": "PXSB030_Yamato_BorgBoss",
      "aliases": [
        "PXSB030_Yamato_BorgBoss",
        "PXSB030",
        "4263458064"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            30
          ],
          "stern": [
            30
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            10,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB053_Aegir_modern": {
      "name": "PXSB053_Aegir_modern",
      "aliases": [
        "PXSB053_Aegir_modern",
        "PXSB053",
        "4239340816"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB054_Yoshino_modern": {
      "name": "PXSB054_Yoshino_modern",
      "aliases": [
        "PXSB054_Yoshino_modern",
        "PXSB054",
        "4238292240"
      ],
      "mainGunCaliberMm": 310,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB055_Michelangelo_modern": {
      "name": "PXSB055_Michelangelo_modern",
      "aliases": [
        "PXSB055_Michelangelo_modern",
        "PXSB055",
        "4237243664"
      ],
      "mainGunCaliberMm": 320,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            40,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB056_Michelangelo_modern2": {
      "name": "PXSB056_Michelangelo_modern2",
      "aliases": [
        "PXSB056_Michelangelo_modern2",
        "PXSB056",
        "4236195088"
      ],
      "mainGunCaliberMm": 320,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            40,
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB101_Amagi_H2020": {
      "name": "PXSB101_Amagi_H2020",
      "aliases": [
        "PXSB101_Amagi_H2020",
        "PXSB101",
        "4189009168"
      ],
      "mainGunCaliberMm": 503,
      "mainGunHePenMm": 205,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32,
            254
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB103_France_H2020": {
      "name": "PXSB103_France_H2020",
      "aliases": [
        "PXSB103_France_H2020",
        "PXSB103",
        "4186912016"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            90,
            120
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSB504_Battleship_Duck_FA2023": {
      "name": "PXSB504_Battleship_Duck_FA2023",
      "aliases": [
        "PXSB504_Battleship_Duck_FA2023",
        "PXSB504",
        "3766433040"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": [
            50
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            1
          ],
          "bow": [
            1
          ],
          "stern": []
        }
      }
    },
    "PXSB506_Battleship_Duck_Two_FA2023": {
      "name": "PXSB506_Battleship_Duck_Two_FA2023",
      "aliases": [
        "PXSB506_Battleship_Duck_Two_FA2023",
        "PXSB506",
        "3764335888"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": [
            50
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            1
          ],
          "bow": [
            1
          ],
          "stern": []
        }
      }
    },
    "PXSC001_Dr_Frankenship": {
      "name": "PXSC001_Dr_Frankenship",
      "aliases": [
        "PXSC001_Dr_Frankenship",
        "PXSC001",
        "4293834000"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 100,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13,
            102
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC002_Charles_Martel_H2017": {
      "name": "PXSC002_Charles_Martel_H2017",
      "aliases": [
        "PXSC002_Charles_Martel_H2017",
        "PXSC002",
        "4292785424"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC003_Pr_68_Chapaev_H2017": {
      "name": "PXSC003_Pr_68_Chapaev_H2017",
      "aliases": [
        "PXSC003_Pr_68_Chapaev_H2017",
        "PXSC003",
        "4291736848"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC004_Galaxy": {
      "name": "PXSC004_Galaxy",
      "aliases": [
        "PXSC004_Galaxy",
        "PXSC004",
        "4290688272"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC005_Zaya": {
      "name": "PXSC005_Zaya",
      "aliases": [
        "PXSC005_Zaya",
        "PXSC005",
        "4289639696"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC006_Norma": {
      "name": "PXSC006_Norma",
      "aliases": [
        "PXSC006_Norma",
        "PXSC006",
        "4288591120"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC007_Aurora": {
      "name": "PXSC007_Aurora",
      "aliases": [
        "PXSC007_Aurora",
        "PXSC007",
        "4287542544"
      ],
      "mainGunCaliberMm": 220,
      "mainGunHePenMm": 37,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            50
          ]
        },
        "side": {
          "values": [
            75
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            100,
            150,
            155
          ],
          "bow": [
            100
          ],
          "stern": [
            150,
            155
          ]
        }
      }
    },
    "PXSC009_Mogami_H2018": {
      "name": "PXSC009_Mogami_H2018",
      "aliases": [
        "PXSC009_Mogami_H2018",
        "PXSC009",
        "4285445392"
      ],
      "mainGunCaliberMm": 155,
      "mainGunHePenMm": 26,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            25,
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC010_Hinden_Apr2019": {
      "name": "PXSC010_Hinden_Apr2019",
      "aliases": [
        "PXSC010_Hinden_Apr2019",
        "PXSC010",
        "4284396816"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PXSC011_Alaska_H2019": {
      "name": "PXSC011_Alaska_H2019",
      "aliases": [
        "PXSC011_Alaska_H2019",
        "PXSC011",
        "4283348240"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            36
          ]
        },
        "side": {
          "values": [
            28
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC012_Hindenburg_H2019": {
      "name": "PXSC012_Hindenburg_H2019",
      "aliases": [
        "PXSC012_Hindenburg_H2019",
        "PXSC012",
        "4282299664"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40
          ],
          "bow": [
            40
          ],
          "stern": []
        }
      }
    },
    "PXSC013_Henri_H2019": {
      "name": "PXSC013_Henri_H2019",
      "aliases": [
        "PXSC013_Henri_H2019",
        "PXSC013",
        "4281251088"
      ],
      "mainGunCaliberMm": 240,
      "mainGunHePenMm": 40,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC016_Monster_Cruiser": {
      "name": "PXSC016_Monster_Cruiser",
      "aliases": [
        "PXSC016_Monster_Cruiser",
        "PXSC016",
        "4278105360"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            30
          ],
          "stern": [
            20
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC027_Fiji_Klingons": {
      "name": "PXSC027_Fiji_Klingons",
      "aliases": [
        "PXSC027_Fiji_Klingons",
        "PXSC027",
        "4266571024"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 32,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13,
            38
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC050_Austin_modern": {
      "name": "PXSC050_Austin_modern",
      "aliases": [
        "PXSC050_Austin_modern",
        "PXSC050",
        "4242453776"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            40
          ],
          "stern": [
            16,
            40
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC051_Dalian_modern": {
      "name": "PXSC051_Dalian_modern",
      "aliases": [
        "PXSC051_Dalian_modern",
        "PXSC051",
        "4241405200"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC052_Ignacio_Allende_modern": {
      "name": "PXSC052_Ignacio_Allende_modern",
      "aliases": [
        "PXSC052_Ignacio_Allende_modern",
        "PXSC052",
        "4240356624"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25,
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC057_Ignacio_Allende_modern2": {
      "name": "PXSC057_Ignacio_Allende_modern2",
      "aliases": [
        "PXSC057_Ignacio_Allende_modern2",
        "PXSC057",
        "4235113744"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25,
            40
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC101_Hindenburg_H2020": {
      "name": "PXSC101_Hindenburg_H2020",
      "aliases": [
        "PXSC101_Hindenburg_H2020",
        "PXSC101",
        "4188976400"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 205,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30,
            110
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40,
            90
          ],
          "bow": [
            40
          ],
          "stern": [
            90
          ]
        }
      }
    },
    "PXSC102_Smolensk_H2020": {
      "name": "PXSC102_Smolensk_H2020",
      "aliases": [
        "PXSC102_Smolensk_H2020",
        "PXSC102",
        "4187927824"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16,
            20
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC121_Des_Moines_Borg_V1": {
      "name": "PXSC121_Des_Moines_Borg_V1",
      "aliases": [
        "PXSC121_Des_Moines_Borg_V1",
        "PXSC121",
        "4168004880"
      ],
      "mainGunCaliberMm": 460,
      "mainGunHePenMm": 70,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            30
          ],
          "stern": [
            30
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC122_Des_Moines_Borg_V2": {
      "name": "PXSC122_Des_Moines_Borg_V2",
      "aliases": [
        "PXSC122_Des_Moines_Borg_V2",
        "PXSC122",
        "4166956304"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            30
          ],
          "stern": [
            30
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC123_Salem_Startrek": {
      "name": "PXSC123_Salem_Startrek",
      "aliases": [
        "PXSC123_Salem_Startrek",
        "PXSC123",
        "4165907728"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 32,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSC501_Cruiser_Duck_FA2023": {
      "name": "PXSC501_Cruiser_Duck_FA2023",
      "aliases": [
        "PXSC501_Cruiser_Duck_FA2023",
        "PXSC501",
        "3769546000"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 305,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": [
            20
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": [
            45
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            1
          ],
          "bow": [
            1
          ],
          "stern": []
        }
      }
    },
    "PXSC502_Cruiser_Duck_Two_FA2023": {
      "name": "PXSC502_Cruiser_Duck_Two_FA2023",
      "aliases": [
        "PXSC502_Cruiser_Duck_Two_FA2023",
        "PXSC502",
        "3768497424"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 305,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": [
            20
          ]
        },
        "deck": {
          "values": [
            20
          ]
        },
        "side": {
          "values": [
            45
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            1
          ],
          "bow": [
            1
          ],
          "stern": []
        }
      }
    },
    "PXSC503_SEABATTLE_CAP": {
      "name": "PXSC503_SEABATTLE_CAP",
      "aliases": [
        "PXSC503_SEABATTLE_CAP",
        "PXSC503",
        "3767448848"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": []
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD001_VanHellsink": {
      "name": "PXSD001_VanHellsink",
      "aliases": [
        "PXSD001_VanHellsink",
        "PXSD001",
        "4293801232"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 100,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            12
          ],
          "stern": [
            12
          ]
        },
        "deck": {
          "values": [
            12
          ]
        },
        "side": {
          "values": [
            12
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD002_Benson_1945_H2017": {
      "name": "PXSD002_Benson_1945_H2017",
      "aliases": [
        "PXSD002_Benson_1945_H2017",
        "PXSD002",
        "4292752656"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD003_Kagero_H2017": {
      "name": "PXSD003_Kagero_H2017",
      "aliases": [
        "PXSD003_Kagero_H2017",
        "PXSD003",
        "4291704080"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD004_FlyFire": {
      "name": "PXSD004_FlyFire",
      "aliases": [
        "PXSD004_FlyFire",
        "PXSD004",
        "4290655504"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD005_Blue_Aster": {
      "name": "PXSD005_Blue_Aster",
      "aliases": [
        "PXSD005_Blue_Aster",
        "PXSD005",
        "4289606928"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD007_Scnellboot_S38": {
      "name": "PXSD007_Scnellboot_S38",
      "aliases": [
        "PXSD007_Scnellboot_S38",
        "PXSD007",
        "4287509776"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD008_Z_23_H2018": {
      "name": "PXSD008_Z_23_H2018",
      "aliases": [
        "PXSD008_Z_23_H2018",
        "PXSD008",
        "4286461200"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD009_Kiev_H2018": {
      "name": "PXSD009_Kiev_H2018",
      "aliases": [
        "PXSD009_Kiev_H2018",
        "PXSD009",
        "4285412624"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD010_Blue_Aster2": {
      "name": "PXSD010_Blue_Aster2",
      "aliases": [
        "PXSD010_Blue_Aster2",
        "PXSD010",
        "4284364048"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD011_FlyFire2": {
      "name": "PXSD011_FlyFire2",
      "aliases": [
        "PXSD011_FlyFire2",
        "PXSD011",
        "4283315472"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD012_Shimakaze2": {
      "name": "PXSD012_Shimakaze2",
      "aliases": [
        "PXSD012_Shimakaze2",
        "PXSD012",
        "4282266896"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD013_Z_52_PA": {
      "name": "PXSD013_Z_52_PA",
      "aliases": [
        "PXSD013_Z_52_PA",
        "PXSD013",
        "4281218320"
      ],
      "mainGunCaliberMm": 128,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD014_Hsiang_Yang_PA": {
      "name": "PXSD014_Hsiang_Yang_PA",
      "aliases": [
        "PXSD014_Hsiang_Yang_PA",
        "PXSD014",
        "4280169744"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD015_Grozovoy_PA": {
      "name": "PXSD015_Grozovoy_PA",
      "aliases": [
        "PXSD015_Grozovoy_PA",
        "PXSD015",
        "4279121168"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD016_Shimakaze_PA": {
      "name": "PXSD016_Shimakaze_PA",
      "aliases": [
        "PXSD016_Shimakaze_PA",
        "PXSD016",
        "4278072592"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD017_Gearing_PA": {
      "name": "PXSD017_Gearing_PA",
      "aliases": [
        "PXSD017_Gearing_PA",
        "PXSD017",
        "4277024016"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19,
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD018_Harugumo_PA": {
      "name": "PXSD018_Harugumo_PA",
      "aliases": [
        "PXSD018_Harugumo_PA",
        "PXSD018",
        "4275975440"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD019_Daring_PA": {
      "name": "PXSD019_Daring_PA",
      "aliases": [
        "PXSD019_Daring_PA",
        "PXSD019",
        "4274926864"
      ],
      "mainGunCaliberMm": 113,
      "mainGunHePenMm": 19,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD020_Khabarovsk_PA": {
      "name": "PXSD020_Khabarovsk_PA",
      "aliases": [
        "PXSD020_Khabarovsk_PA",
        "PXSD020",
        "4273878288"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 51,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            25,
            50
          ],
          "stern": [
            19,
            25,
            50
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD021_Kleber_PA": {
      "name": "PXSD021_Kleber_PA",
      "aliases": [
        "PXSD021_Kleber_PA",
        "PXSD021",
        "4272829712"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD022_Shimakaze_H2019": {
      "name": "PXSD022_Shimakaze_H2019",
      "aliases": [
        "PXSD022_Shimakaze_H2019",
        "PXSD022",
        "4271781136"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD023_Gearing_H2019": {
      "name": "PXSD023_Gearing_H2019",
      "aliases": [
        "PXSD023_Gearing_H2019",
        "PXSD023",
        "4270732560"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19,
            21
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD024_Khabarovsk_H2019": {
      "name": "PXSD024_Khabarovsk_H2019",
      "aliases": [
        "PXSD024_Khabarovsk_H2019",
        "PXSD024",
        "4269683984"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            25,
            50
          ],
          "stern": [
            19,
            25,
            50
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            50
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD025_Berserk": {
      "name": "PXSD025_Berserk",
      "aliases": [
        "PXSD025_Berserk",
        "PXSD025",
        "4268635408"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": []
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD027_Akatsuki_Romulans": {
      "name": "PXSD027_Akatsuki_Romulans",
      "aliases": [
        "PXSD027_Akatsuki_Romulans",
        "PXSD027",
        "4266538256"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 40,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD031_Gearing_Borg_V1": {
      "name": "PXSD031_Gearing_Borg_V1",
      "aliases": [
        "PXSD031_Gearing_Borg_V1",
        "PXSD031",
        "4262343952"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 32,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            30
          ],
          "stern": [
            10,
            30
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD032_Gearing_Borg_V2": {
      "name": "PXSD032_Gearing_Borg_V2",
      "aliases": [
        "PXSD032_Gearing_Borg_V2",
        "PXSD032",
        "4261295376"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            30
          ],
          "stern": [
            10,
            30
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD041_Marceau_modern": {
      "name": "PXSD041_Marceau_modern",
      "aliases": [
        "PXSD041_Marceau_modern",
        "PXSD041",
        "4251858192"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19,
            20
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            20
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD042_Grozovoy_modern": {
      "name": "PXSD042_Grozovoy_modern",
      "aliases": [
        "PXSD042_Grozovoy_modern",
        "PXSD042",
        "4250809616"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            15,
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD043_Jutland_modern": {
      "name": "PXSD043_Jutland_modern",
      "aliases": [
        "PXSD043_Jutland_modern",
        "PXSD043",
        "4249761040"
      ],
      "mainGunCaliberMm": 113,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD056_Jutland_modern2": {
      "name": "PXSD056_Jutland_modern2",
      "aliases": [
        "PXSD056_Jutland_modern2",
        "PXSD056",
        "4236129552"
      ],
      "mainGunCaliberMm": 113,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD102_Akizuki_H2020": {
      "name": "PXSD102_Akizuki_H2020",
      "aliases": [
        "PXSD102_Akizuki_H2020",
        "PXSD102",
        "4187895056"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19,
            20
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD103_Oland_H2020": {
      "name": "PXSD103_Oland_H2020",
      "aliases": [
        "PXSD103_Oland_H2020",
        "PXSD103",
        "4186846480"
      ],
      "mainGunCaliberMm": 139,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD502_Destroyer_Duck_FA2023": {
      "name": "PXSD502_Destroyer_Duck_FA2023",
      "aliases": [
        "PXSD502_Destroyer_Duck_FA2023",
        "PXSD502",
        "3768464656"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 305,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            1
          ],
          "stern": [
            1
          ]
        },
        "deck": {
          "values": [
            1
          ]
        },
        "side": {
          "values": [
            1
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSD503_Destroyer_Duck_Two_FA2023": {
      "name": "PXSD503_Destroyer_Duck_Two_FA2023",
      "aliases": [
        "PXSD503_Destroyer_Duck_Two_FA2023",
        "PXSD503",
        "3767416080"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 305,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            1
          ],
          "stern": [
            1
          ]
        },
        "deck": {
          "values": [
            1
          ]
        },
        "side": {
          "values": [
            1
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSS107_Mina_Hurray": {
      "name": "PXSS107_Mina_Hurray",
      "aliases": [
        "PXSS107_Mina_Hurray",
        "PXSS107",
        "4182160656"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            13,
            16
          ],
          "stern": [
            10,
            13,
            16
          ]
        },
        "deck": {
          "values": [
            10,
            13,
            16
          ]
        },
        "side": {
          "values": [
            10,
            13,
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSS207_Lazarus_Centurio": {
      "name": "PXSS207_Lazarus_Centurio",
      "aliases": [
        "PXSS207_Lazarus_Centurio",
        "PXSS207",
        "4077303056"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSS307_Cyrus_Herrero": {
      "name": "PXSS307_Cyrus_Herrero",
      "aliases": [
        "PXSS307_Cyrus_Herrero",
        "PXSS307",
        "3972445456"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSS407_Dr_Frankenship": {
      "name": "PXSS407_Dr_Frankenship",
      "aliases": [
        "PXSS407_Dr_Frankenship",
        "PXSS407",
        "3867587856"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13,
            16,
            19
          ],
          "stern": [
            13,
            16,
            19
          ]
        },
        "deck": {
          "values": [
            13,
            16,
            19
          ]
        },
        "side": {
          "values": [
            13,
            16,
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSS507_Klaus_V_Teslau": {
      "name": "PXSS507_Klaus_V_Teslau",
      "aliases": [
        "PXSS507_Klaus_V_Teslau",
        "PXSS507",
        "3762730256"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16,
            19,
            25
          ],
          "stern": [
            16,
            19,
            25
          ]
        },
        "deck": {
          "values": [
            16,
            19,
            25
          ]
        },
        "side": {
          "values": [
            16,
            19,
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX001_Transylvania": {
      "name": "PXSX001_Transylvania",
      "aliases": [
        "PXSX001_Transylvania",
        "PXSX001",
        "4293145872"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX016_Goliath": {
      "name": "PXSX016_Goliath",
      "aliases": [
        "PXSX016_Goliath",
        "PXSX016",
        "4277417232"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX017_Caboteur_de_35_metres": {
      "name": "PXSX017_Caboteur_de_35_metres",
      "aliases": [
        "PXSX017_Caboteur_de_35_metres",
        "PXSX017",
        "4276368656"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX023_HMS_SS_Lorina": {
      "name": "PXSX023_HMS_SS_Lorina",
      "aliases": [
        "PXSX023_HMS_SS_Lorina",
        "PXSX023",
        "4270077200"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX024_Aronia": {
      "name": "PXSX024_Aronia",
      "aliases": [
        "PXSX024_Aronia",
        "PXSX024",
        "4269028624"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX025_Medway_Queen": {
      "name": "PXSX025_Medway_Queen",
      "aliases": [
        "PXSX025_Medway_Queen",
        "PXSX025",
        "4267980048"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX026_Canterbury": {
      "name": "PXSX026_Canterbury",
      "aliases": [
        "PXSX026_Canterbury",
        "PXSX026",
        "4266931472"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX033_Dyck": {
      "name": "PXSX033_Dyck",
      "aliases": [
        "PXSX033_Dyck",
        "PXSX033",
        "4259591440"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX034_John_Cattling": {
      "name": "PXSX034_John_Cattling",
      "aliases": [
        "PXSX034_John_Cattling",
        "PXSX034",
        "4258542864"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX035_Landing_Ship_1": {
      "name": "PXSX035_Landing_Ship_1",
      "aliases": [
        "PXSX035_Landing_Ship_1",
        "PXSX035",
        "4257494288"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX037_Daihatsu": {
      "name": "PXSX037_Daihatsu",
      "aliases": [
        "PXSX037_Daihatsu",
        "PXSX037",
        "4255397136"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX039_LST_325": {
      "name": "PXSX039_LST_325",
      "aliases": [
        "PXSX039_LST_325",
        "PXSX039",
        "4253299984"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX040_Escort_8": {
      "name": "PXSX040_Escort_8",
      "aliases": [
        "PXSX040_Escort_8",
        "PXSX040",
        "4252251408"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX043_Medway_Queen_War": {
      "name": "PXSX043_Medway_Queen_War",
      "aliases": [
        "PXSX043_Medway_Queen_War",
        "PXSX043",
        "4249105680"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX044_Cimarron": {
      "name": "PXSX044_Cimarron",
      "aliases": [
        "PXSX044_Cimarron",
        "PXSX044",
        "4248057104"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            14
          ],
          "stern": [
            10,
            13,
            14
          ]
        },
        "deck": {
          "values": [
            14
          ]
        },
        "side": {
          "values": [
            18
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX045_Liberty": {
      "name": "PXSX045_Liberty",
      "aliases": [
        "PXSX045_Liberty",
        "PXSX045",
        "4247008528"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            14
          ],
          "stern": [
            10,
            13
          ]
        },
        "deck": {
          "values": [
            14
          ]
        },
        "side": {
          "values": [
            18
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX047_Golo": {
      "name": "PXSX047_Golo",
      "aliases": [
        "PXSX047_Golo",
        "PXSX047",
        "4244911376"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            14
          ],
          "stern": [
            10,
            13,
            14
          ]
        },
        "deck": {
          "values": [
            14
          ]
        },
        "side": {
          "values": [
            18
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX501_LIBERTY_ARM": {
      "name": "PXSX501_LIBERTY_ARM",
      "aliases": [
        "PXSX501_LIBERTY_ARM",
        "PXSX501",
        "3768857872"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX502_LIBERTY_ARM_CONVOY": {
      "name": "PXSX502_LIBERTY_ARM_CONVOY",
      "aliases": [
        "PXSX502_LIBERTY_ARM_CONVOY",
        "PXSX502",
        "3767809296"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX743_Hall_Medway_Queen": {
      "name": "PXSX743_Hall_Medway_Queen",
      "aliases": [
        "PXSX743_Hall_Medway_Queen",
        "PXSX743",
        "3515102480"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [],
          "stern": []
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PXSX815_Bogue_Clone": {
      "name": "PXSX815_Bogue_Clone",
      "aliases": [
        "PXSX815_Bogue_Clone",
        "PXSX815",
        "3439605008"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            10,
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSA508_Saipan_Sanzang": {
      "name": "PZSA508_Saipan_Sanzang",
      "aliases": [
        "PZSA508_Saipan_Sanzang",
        "PZSA508",
        "3762271440"
      ],
      "mainGunCaliberMm": None,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSB509_Izumo_Bajie": {
      "name": "PZSB509_Izumo_Bajie",
      "aliases": [
        "PZSB509_Izumo_Bajie",
        "PZSB509",
        "3761190096"
      ],
      "mainGunCaliberMm": 410,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            57
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSB519_Alsace_Wujing": {
      "name": "PZSB519_Alsace_Wujing",
      "aliases": [
        "PZSB519_Alsace_Wujing",
        "PZSB519",
        "3750704336"
      ],
      "mainGunCaliberMm": 380,
      "mainGunHePenMm": 63,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSB529_Sun_Yat_Sen": {
      "name": "PZSB529_Sun_Yat_Sen",
      "aliases": [
        "PZSB529_Sun_Yat_Sen",
        "PZSB529",
        "3740218576"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32,
            40,
            60
          ]
        },
        "deck": {
          "values": [
            60
          ]
        },
        "side": {
          "values": [
            60,
            375
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            180,
            220,
            375,
            420
          ],
          "bow": [
            220,
            420
          ],
          "stern": [
            180,
            375
          ]
        }
      }
    },
    "PZSB539_Louchuan": {
      "name": "PZSB539_Louchuan",
      "aliases": [
        "PZSB539_Louchuan",
        "PZSB539",
        "3729732816"
      ],
      "mainGunCaliberMm": 419,
      "mainGunHePenMm": 105,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32,
            381
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSB707_Teng_She": {
      "name": "PZSB707_Teng_She",
      "aliases": [
        "PZSB707_Teng_She",
        "PZSB707",
        "3553572048"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            26,
            35
          ],
          "stern": [
            26
          ]
        },
        "deck": {
          "values": [
            26
          ]
        },
        "side": {
          "values": [
            26,
            100
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            30,
            200
          ],
          "bow": [
            200
          ],
          "stern": [
            30
          ]
        }
      }
    },
    "PZSB708_Xuan_Wu": {
      "name": "PZSB708_Xuan_Wu",
      "aliases": [
        "PZSB708_Xuan_Wu",
        "PZSB708",
        "3552523472"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            38
          ]
        },
        "side": {
          "values": [
            38
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSB709_Taihang": {
      "name": "PZSB709_Taihang",
      "aliases": [
        "PZSB709_Taihang",
        "PZSB709",
        "3551474896"
      ],
      "mainGunCaliberMm": 406,
      "mainGunHePenMm": 68,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            32
          ]
        },
        "side": {
          "values": [
            32,
            45
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSB719_Yimeng": {
      "name": "PZSB719_Yimeng",
      "aliases": [
        "PZSB719_Yimeng",
        "PZSB719",
        "3540989136"
      ],
      "mainGunCaliberMm": 356,
      "mainGunHePenMm": 59,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            200
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            200
          ],
          "bow": [
            200
          ],
          "stern": [
            200
          ]
        }
      }
    },
    "PZSB909_Xuan_Ming": {
      "name": "PZSB909_Xuan_Ming",
      "aliases": [
        "PZSB909_Xuan_Ming",
        "PZSB909",
        "3341759696"
      ],
      "mainGunCaliberMm": 457,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            32
          ],
          "stern": [
            32,
            40,
            60
          ]
        },
        "deck": {
          "values": [
            60
          ]
        },
        "side": {
          "values": [
            60,
            375
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            180,
            220,
            375,
            420
          ],
          "bow": [
            220,
            420
          ],
          "stern": [
            180,
            375
          ]
        }
      }
    },
    "PZSC101_Cheng_An": {
      "name": "PZSC101_Cheng_An",
      "aliases": [
        "PZSC101_Cheng_An",
        "PZSC101",
        "4188976336"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC105_Chung_King": {
      "name": "PZSC105_Chung_King",
      "aliases": [
        "PZSC105_Chung_King",
        "PZSC105",
        "4184782032"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13,
            25
          ]
        },
        "side": {
          "values": [
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC106_Rahmat": {
      "name": "PZSC106_Rahmat",
      "aliases": [
        "PZSC106_Rahmat",
        "PZSC106",
        "4183733456"
      ],
      "mainGunCaliberMm": 133,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13,
            25
          ]
        },
        "side": {
          "values": [
            13,
            89
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC107_Chumphon": {
      "name": "PZSC107_Chumphon",
      "aliases": [
        "PZSC107_Chumphon",
        "PZSC107",
        "4182684880"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            13
          ],
          "stern": [
            13
          ]
        },
        "deck": {
          "values": [
            13
          ]
        },
        "side": {
          "values": [
            13
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC108_Harbin": {
      "name": "PZSC108_Harbin",
      "aliases": [
        "PZSC108_Harbin",
        "PZSC108",
        "4181636304"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC109_Sejong": {
      "name": "PZSC109_Sejong",
      "aliases": [
        "PZSC109_Sejong",
        "PZSC109",
        "4180587728"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC110_Jinan": {
      "name": "PZSC110_Jinan",
      "aliases": [
        "PZSC110_Jinan",
        "PZSC110",
        "4179539152"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            32
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC503_Ning_Hai": {
      "name": "PZSC503_Ning_Hai",
      "aliases": [
        "PZSC503_Ning_Hai",
        "PZSC503",
        "3767448784"
      ],
      "mainGunCaliberMm": 140,
      "mainGunHePenMm": 23,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": []
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC506_Huang_he": {
      "name": "PZSC506_Huang_he",
      "aliases": [
        "PZSC506_Huang_he",
        "PZSC506",
        "3764303056"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 25,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            70
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC508_Irian": {
      "name": "PZSC508_Irian",
      "aliases": [
        "PZSC508_Irian",
        "PZSC508",
        "3762205904"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC509_Dalian": {
      "name": "PZSC509_Dalian",
      "aliases": [
        "PZSC509_Dalian",
        "PZSC509",
        "3761157328"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC518_Martel_Wukong": {
      "name": "PZSC518_Martel_Wukong",
      "aliases": [
        "PZSC518_Martel_Wukong",
        "PZSC518",
        "3751720144"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            27
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC529_Mengchong": {
      "name": "PZSC529_Mengchong",
      "aliases": [
        "PZSC529_Mengchong",
        "PZSC529",
        "3740185808"
      ],
      "mainGunCaliberMm": 305,
      "mainGunHePenMm": 76,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            27
          ],
          "stern": [
            27
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            90
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC710_Incheon": {
      "name": "PZSC710_Incheon",
      "aliases": [
        "PZSC710_Incheon",
        "PZSC710",
        "3550393552"
      ],
      "mainGunCaliberMm": 203,
      "mainGunHePenMm": 34,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC717_Lanzhou": {
      "name": "PZSC717_Lanzhou",
      "aliases": [
        "PZSC717_Lanzhou",
        "PZSC717",
        "3543053520"
      ],
      "mainGunCaliberMm": 180,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            25
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC718_Narai": {
      "name": "PZSC718_Narai",
      "aliases": [
        "PZSC718_Narai",
        "PZSC718",
        "3542004944"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC719_Tianjin": {
      "name": "PZSC719_Tianjin",
      "aliases": [
        "PZSC719_Tianjin",
        "PZSC719",
        "3540956368"
      ],
      "mainGunCaliberMm": 220,
      "mainGunHePenMm": 37,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            40
          ]
        },
        "side": {
          "values": [
            35
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            40,
            130
          ],
          "bow": [
            40
          ],
          "stern": [
            40,
            130
          ]
        }
      }
    },
    "PZSC720_Zhuge_Liang": {
      "name": "PZSC720_Zhuge_Liang",
      "aliases": [
        "PZSC720_Zhuge_Liang",
        "PZSC720",
        "3539907792"
      ],
      "mainGunCaliberMm": 330,
      "mainGunHePenMm": 55,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25,
            30
          ]
        },
        "deck": {
          "values": [
            36
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC729_Baotou": {
      "name": "PZSC729_Baotou",
      "aliases": [
        "PZSC729_Baotou",
        "PZSC729",
        "3530470608"
      ],
      "mainGunCaliberMm": 180,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            30
          ]
        },
        "side": {
          "values": [
            30
          ]
        },
        "extendedBowSternBelt": {
          "present": True,
          "values": [
            50
          ],
          "bow": [
            50
          ],
          "stern": [
            50
          ]
        }
      }
    },
    "PZSC908_Pinata_Irian": {
      "name": "PZSC908_Pinata_Irian",
      "aliases": [
        "PZSC908_Pinata_Irian",
        "PZSC908",
        "3342775504"
      ],
      "mainGunCaliberMm": 152,
      "mainGunHePenMm": 30,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            25
          ],
          "stern": [
            25
          ]
        },
        "deck": {
          "values": [
            27
          ]
        },
        "side": {
          "values": [
            25
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSC918_Azur_Harbin": {
      "name": "PZSC918_Azur_Harbin",
      "aliases": [
        "PZSC918_Azur_Harbin",
        "PZSC918",
        "3332289744"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD102_Long_Jiang": {
      "name": "PZSD102_Long_Jiang",
      "aliases": [
        "PZSD102_Long_Jiang",
        "PZSD102",
        "4187894992"
      ],
      "mainGunCaliberMm": 105,
      "mainGunHePenMm": 18,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6,
            9
          ],
          "stern": [
            6,
            9
          ]
        },
        "deck": {
          "values": [
            9
          ]
        },
        "side": {
          "values": [
            6,
            9
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD103_Phra_Ruang": {
      "name": "PZSD103_Phra_Ruang",
      "aliases": [
        "PZSD103_Phra_Ruang",
        "PZSD103",
        "4186846416"
      ],
      "mainGunCaliberMm": 102,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            6
          ],
          "stern": [
            6
          ]
        },
        "deck": {
          "values": [
            6
          ]
        },
        "side": {
          "values": [
            6
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD104_Shen_Yang": {
      "name": "PZSD104_Shen_Yang",
      "aliases": [
        "PZSD104_Shen_Yang",
        "PZSD104",
        "4185797840"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10,
            14
          ],
          "stern": [
            10,
            12,
            14
          ]
        },
        "deck": {
          "values": [
            14
          ]
        },
        "side": {
          "values": [
            14
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD105_Jian_Wei": {
      "name": "PZSD105_Jian_Wei",
      "aliases": [
        "PZSD105_Jian_Wei",
        "PZSD105",
        "4184749264"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            10
          ],
          "stern": [
            10
          ]
        },
        "deck": {
          "values": [
            10
          ]
        },
        "side": {
          "values": [
            10
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD106_Fu_Shun": {
      "name": "PZSD106_Fu_Shun",
      "aliases": [
        "PZSD106_Fu_Shun",
        "PZSD106",
        "4183700688"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16,
            19
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD107_Gadjah_Mada": {
      "name": "PZSD107_Gadjah_Mada",
      "aliases": [
        "PZSD107_Gadjah_Mada",
        "PZSD107",
        "4182652112"
      ],
      "mainGunCaliberMm": 120,
      "mainGunHePenMm": 20,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD108_Hsien_Yang": {
      "name": "PZSD108_Hsien_Yang",
      "aliases": [
        "PZSD108_Hsien_Yang",
        "PZSD108",
        "4181603536"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19,
            20
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD109_Chung_Mu": {
      "name": "PZSD109_Chung_Mu",
      "aliases": [
        "PZSD109_Chung_Mu",
        "PZSD109",
        "4180554960"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD110_Hsiang_Yang": {
      "name": "PZSD110_Hsiang_Yang",
      "aliases": [
        "PZSD110_Hsiang_Yang",
        "PZSD110",
        "4179506384"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD111_Kunming": {
      "name": "PZSD111_Kunming",
      "aliases": [
        "PZSD111_Kunming",
        "PZSD111",
        "4178457808"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD208_Siliwangi_1959": {
      "name": "PZSD208_Siliwangi_1959",
      "aliases": [
        "PZSD208_Siliwangi_1959",
        "PZSD208",
        "4076745936"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD506_Anshan": {
      "name": "PZSD506_Anshan",
      "aliases": [
        "PZSD506_Anshan",
        "PZSD506",
        "3764270288"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            16
          ],
          "stern": [
            16,
            19
          ]
        },
        "deck": {
          "values": [
            16
          ]
        },
        "side": {
          "values": [
            16
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD508_LoYang": {
      "name": "PZSD508_LoYang",
      "aliases": [
        "PZSD508_LoYang",
        "PZSD508",
        "3762173136"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD510_Lushun": {
      "name": "PZSD510_Lushun",
      "aliases": [
        "PZSD510_Lushun",
        "PZSD510",
        "3760075984"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD518_Fen_Yang": {
      "name": "PZSD518_Fen_Yang",
      "aliases": [
        "PZSD518_Fen_Yang",
        "PZSD518",
        "3751687376"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD598_Black_LoYang": {
      "name": "PZSD598_Black_LoYang",
      "aliases": [
        "PZSD598_Black_LoYang",
        "PZSD598",
        "3667801296"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD708_Zhu_Que": {
      "name": "PZSD708_Zhu_Que",
      "aliases": [
        "PZSD708_Zhu_Que",
        "PZSD708",
        "3552457936"
      ],
      "mainGunCaliberMm": 127,
      "mainGunHePenMm": 21,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD718_Warhammer_Ork": {
      "name": "PZSD718_Warhammer_Ork",
      "aliases": [
        "PZSD718_Warhammer_Ork",
        "PZSD718",
        "3541972176"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": 17,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD719_Nanning": {
      "name": "PZSD719_Nanning",
      "aliases": [
        "PZSD719_Nanning",
        "PZSD719",
        "3540923600"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSD910_Black_Lushun": {
      "name": "PZSD910_Black_Lushun",
      "aliases": [
        "PZSD910_Black_Lushun",
        "PZSD910",
        "3340645584"
      ],
      "mainGunCaliberMm": 130,
      "mainGunHePenMm": 22,
      "mainGunSapPenMm": None,
      "armor": {
        "bowStern": {
          "bow": [
            19
          ],
          "stern": [
            19
          ]
        },
        "deck": {
          "values": [
            19
          ]
        },
        "side": {
          "values": [
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    },
    "PZSS716_Xing_Zhong_Guo_14": {
      "name": "PZSS716_Xing_Zhong_Guo_14",
      "aliases": [
        "PZSS716_Xing_Zhong_Guo_14",
        "PZSS716",
        "3543577808"
      ],
      "mainGunCaliberMm": 100,
      "mainGunHePenMm": None,
      "mainGunSapPenMm": 29,
      "armor": {
        "bowStern": {
          "bow": [
            13,
            16,
            19
          ],
          "stern": [
            13,
            16,
            19
          ]
        },
        "deck": {
          "values": [
            13,
            16,
            19
          ]
        },
        "side": {
          "values": [
            13,
            16,
            19
          ]
        },
        "extendedBowSternBelt": {
          "present": False,
          "values": [],
          "bow": [],
          "stern": []
        }
      }
    }
  }
}
