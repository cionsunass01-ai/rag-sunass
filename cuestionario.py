# rag_sunass/cuestionario.py

CUESTIONARIO_SUNASS = [

    # ── BLOQUE 1: IDENTIFICACIÓN (3 variables) ────────────────────────
    {
        "id": 1, "bloque": "Identificación", "variable": "CUTF",
        "descripcion": "Código Único de Trámite o Expediente",
        "es_encabezado": True,
        "keywords": ["CUTF", "código único", "expediente", "trámite",
                     "número de expediente", "referencia", "código", "N°"],
        "query_busqueda": "CUTF código único trámite expediente número referencia identificador",
    },
    {
        "id": 2, "bloque": "Identificación", "variable": "SISTRAM_ID",
        "descripcion": "ID numérico en el sistema de trámite documentario",
        "es_encabezado": True,
        "keywords": ["SISTRAM", "sistema de trámite", "ID", "registro",
                     "número de registro", "sistema documentario", "folio", "ingreso"],
        "query_busqueda": "SISTRAM ID sistema trámite documentario registro número ingreso folio",
    },
    {
        "id": 3, "bloque": "Identificación", "variable": "EP_Nombre",
        "descripcion": "Nombre completo de la Empresa Prestadora fiscalizada",
        "keywords": ["empresa prestadora", "EPS", "SEDAPAL", "EMAPA", "SEDAM",
                     "operador", "prestador", "denominación", "razón social"],
        "query_busqueda": "empresa prestadora EPS nombre completo razón social operador servicios saneamiento",
    },

    # ── BLOQUE 2: PRÓRROGA (4 variables) ─────────────────────────────
    {
        "id": 4, "bloque": "Prórroga", "variable": "Solicitud_Prorroga",
        "descripcion": "Indica si la EP solicitó prórroga (Sí/No)",
        "keywords": ["prórroga", "solicita prórroga", "solicitud de prórroga",
                     "ampliación", "mayor plazo", "extensión de plazo"],
        "query_busqueda": "solicita prórroga ampliación de plazo extensión tiempo adicional EP solicitó",
    },
    {
        "id": 5, "bloque": "Prórroga", "variable": "Prorroga_Dias",
        "descripcion": "Cantidad de días de prórroga solicitados",
        "keywords": ["días", "días hábiles", "días calendario", "plazo de",
                     "por un período", "días adicionales", "prórroga de"],
        "query_busqueda": "número días prórroga solicitados período adicional días hábiles calendario plazo",
    },
    {
        "id": 6, "bloque": "Prórroga", "variable": "Prorroga_Motivo",
        "descripcion": "Justificación textual de la solicitud de prórroga",
        "keywords": ["motivo", "justificación", "razón", "debido a", "en virtud",
                     "volumen", "complejidad", "dificultad", "porque", "toda vez"],
        "query_busqueda": "motivo justificación razón solicitud prórroga debido a volumen información complejidad",
    },
    {
        "id": 7, "bloque": "Prórroga", "variable": "Prorroga_Estado",
        "descripcion": "Estado de la prórroga: Concedida / Denegada / Aceptada",
        "keywords": ["concedida", "denegada", "aceptada", "aprobada", "rechazada",
                     "no ha lugar", "se otorga", "se acepta", "se deniega"],
        "query_busqueda": "prórroga concedida denegada aceptada aprobada rechazada no ha lugar SUNASS resuelve",
    },

    # ── BLOQUE 3: INFORMACIÓN ADICIONAL (3 variables) ─────────────────
    {
        "id": 8, "bloque": "Información Adicional", "variable": "Info_Extra_Requerida",
        "descripcion": "Detalle de información adicional solicitada a la EP",
        "keywords": ["información adicional", "documentación adicional", "requiere",
                     "solicita información", "adjuntar", "remitir", "enviar",
                     "reportes", "informes técnicos", "sustento"],
        "query_busqueda": "información adicional documentación requerida solicita adjuntar remitir enviar reportes",
    },
    {
        "id": 9, "bloque": "Información Adicional", "variable": "Doc_Ref_Extra",
        "descripcion": "Número de oficio que solicita la información extra",
        "keywords": ["oficio", "mediante oficio", "con oficio", "N° oficio",
                     "carta", "memorándum", "requerimiento", "solicitud"],
        "query_busqueda": "número oficio carta memorándum documento que solicita información adicional referencia",
    },
    {
        "id": 10, "bloque": "Información Adicional", "variable": "Fecha_Limite_Extra",
        "descripcion": "Nueva fecha límite de entrega de información adicional",
        "keywords": ["fecha límite", "hasta el", "plazo vence", "nueva fecha",
                     "fecha de entrega", "fecha máxima", "vencimiento"],
        "query_busqueda": "fecha límite nueva entrega información adicional hasta el vencimiento plazo máximo",
    },

    # ── BLOQUE 4: COMPETENCIA Y ORIGEN (3 variables) ──────────────────
    {
        "id": 11, "bloque": "Competencia y Origen", "variable": "Competencia_Sunass",
        "descripcion": "Competencia de SUNASS para el caso: SI / NO / PROCEDE",
        "keywords": ["competencia", "competente", "jurisdicción", "facultad",
                     "atribución", "corresponde a SUNASS", "PROCEDE"],
        "query_busqueda": "SUNASS competente competencia jurisdicción facultad corresponde atribución PROCEDE",
    },
    {
        "id": 12, "bloque": "Competencia y Origen", "variable": "Tipo_Origen",
        "descripcion": "Origen de la fiscalización: Programación / Denuncia / De oficio",
        "keywords": ["programación", "denuncia", "de oficio", "plan anual",
                     "queja", "reclamo", "iniciativa", "programada"],
        "query_busqueda": "origen proceso fiscalización programación anual denuncia de oficio queja reclamo",
    },
    {
        "id": 13, "bloque": "Competencia y Origen", "variable": "Plazo_Subsanacion",
        "descripcion": "Días otorgados para subsanar observaciones",
        "keywords": ["plazo de subsanación", "subsanar", "días para subsanar",
                     "observaciones", "levantar observaciones", "subsanación"],
        "query_busqueda": "plazo subsanación días para subsanar observaciones levantar plazo otorgado",
    },

    # ── BLOQUE 5: EJECUCIÓN (5 variables) ─────────────────────────────
    {
        "id": 14, "bloque": "Ejecución", "variable": "Plan_Num",
        "descripcion": "Número del Plan de Trabajo aprobado",
        "keywords": ["plan de trabajo", "PT-", "plan N°", "plan aprobado",
                     "plan de fiscalización", "plan número"],
        "query_busqueda": "número plan de trabajo aprobado PT fiscalización plan N° identificador",
    },
    {
        "id": 15, "bloque": "Ejecución", "variable": "Meta_Gestion",
        "descripcion": "Indicador o meta de gestión bajo fiscalización",
        "keywords": ["meta", "indicador", "continuidad", "presión de red",
                     "cloro residual", "ANF", "calidad", "cobertura",
                     "micromedición", "morosidad"],
        "query_busqueda": "indicador meta gestión continuidad presión red cloro agua facturada ANF cobertura",
    },
    {
        "id": 16, "bloque": "Ejecución", "variable": "Modalidad",
        "descripcion": "Modalidad de ejecución: Sede (documental) / Campo (visita)",
        "keywords": ["modalidad", "sede", "campo", "gabinete", "presencial",
                     "documental", "visita in situ", "acción de campo"],
        "query_busqueda": "modalidad fiscalización sede campo gabinete documental presencial visita in situ",
    },
    {
        "id": 17, "bloque": "Ejecución", "variable": "Fecha_Campo",
        "descripcion": "Fecha de ejecución de la acción de campo",
        "keywords": ["fecha de campo", "fecha de visita", "se realizó el",
                     "acción de campo", "se ejecutó", "visita realizada"],
        "query_busqueda": "fecha visita campo inspección se realizó acción de campo se ejecutó fecha",
    },
    {
        "id": 18, "bloque": "Ejecución", "variable": "Acta_Fiscalizacion",
        "descripcion": "Número del Acta de Fiscalización de campo",
        "keywords": ["acta", "acta de fiscalización", "acta N°", "acta número",
                     "número de acta", "acta de campo", "acta de inspección"],
        "query_busqueda": "acta fiscalización número acta campo inspección N° acta de visita generada",
    },

    # ── BLOQUE 6: HALLAZGOS Y RESPONSABLES (4 variables) ──────────────
    {
        "id": 19, "bloque": "Hallazgos y Responsables", "variable": "Indicio_Incumplimiento",
        "descripcion": "Indica si hay hallazgos de falta normativa: SI / NO",
        "keywords": ["incumplimiento", "indicio", "hallazgo", "infracción",
                     "se verificó", "se constató", "vulnera", "no cumple",
                     "se ha determinado", "evidencia"],
        "query_busqueda": "indicio incumplimiento hallazgo infracción se verificó no cumple vulnera evidencia",
    },
    {
        "id": 20, "bloque": "Hallazgos y Responsables", "variable": "Informe_Num",
        "descripcion": "Número del Informe de Fiscalización",
        "keywords": ["informe N°", "informe número", "informe de fiscalización",
                     "número de informe", "informe técnico", "el presente informe"],
        "query_busqueda": "número informe fiscalización N° informe técnico presente informe identificador",
    },
    {
        "id": 21, "bloque": "Hallazgos y Responsables", "variable": "Analista_Responsable",
        "descripcion": "Nombre del Especialista/Analista de la DF a cargo",
        "keywords": ["analista", "especialista", "elaborado por", "a cargo",
                     "responsable", "preparado por", "especialista DF"],
        "query_busqueda": "analista especialista elaborado por nombre responsable cargo DF preparado",
    },
    {
        "id": 22, "bloque": "Hallazgos y Responsables", "variable": "Coordinador_Vto",
        "descripcion": "Nombre del Coordinador Temático que dio visto bueno",
        "keywords": ["coordinador", "visto bueno", "Vo.Bo.", "coordinador temático",
                     "revisado por", "aprobado por", "conforme", "VB"],
        "query_busqueda": "coordinador temático visto bueno Vo.Bo. VB revisado aprobado firma coordinador",
    },

    # ── BLOQUE 7: DETERMINACIÓN Y CIERRE (7 variables) ────────────────
    {
        "id": 23, "bloque": "Determinación y Cierre", "variable": "Accion_Sugerida",
        "descripcion": "Acción sugerida: IMC / IRAST / Archivo",
        "keywords": ["IMC", "IRAST", "medida correctiva", "incremento de tarifa",
                     "archivo", "se recomienda", "se sugiere", "PAS"],
        "query_busqueda": "acción sugerida IMC IRAST medida correctiva incremento tarifa archivo se recomienda",
    },
    {
        "id": 24, "bloque": "Determinación y Cierre", "variable": "Infraccion_Tipo",
        "descripcion": "Código de la infracción tipificada en el reglamento",
        "keywords": ["artículo", "numeral", "literal", "reglamento", "tipificada",
                     "infracción", "norma aplicable", "código de infracción"],
        "query_busqueda": "artículo numeral literal reglamento tipificada infracción código norma aplicable",
    },
    {
        "id": 25, "bloque": "Determinación y Cierre", "variable": "Monto_Multa",
        "descripcion": "Monto de multa en UIT (si aplica incremento tarifario)",
        "keywords": ["multa", "UIT", "sanción", "monto", "penalidad",
                     "importe", "unidad impositiva", "S/.", "soles"],
        "query_busqueda": "monto multa UIT sanción económica penalidad importe unidad impositiva tributaria",
    },
    {
        "id": 26, "bloque": "Determinación y Cierre", "variable": "Estado_Expediente",
        "descripcion": "Estado final del expediente: Archivo / Derivado / PAS",
        "keywords": ["archivo", "archívese", "derivado", "PAS", "conclusión",
                     "cierre", "se da por", "expediente concluido", "derivación"],
        "query_busqueda": "estado expediente archívese concluido derivado PAS cierre se da por archivo",
    },
    {
        "id": 27, "bloque": "Determinación y Cierre", "variable": "Fecha_Notificacion",
        "descripcion": "Fecha de notificación del resultado al prestador",
        "keywords": ["fecha de notificación", "notificado", "comunicado",
                     "se notificó", "se comunicó", "notificación"],
        "query_busqueda": "fecha notificación comunicación al prestador se notificó se comunicó resultado",
    },
    {
        "id": 28, "bloque": "Determinación y Cierre", "variable": "Folios",
        "descripcion": "Cantidad de folios del expediente",
        "keywords": ["folios", "folio", "páginas", "número de folios",
                     "consta de", "total de folios"],
        "query_busqueda": "folios número total páginas expediente consta de folio",
    },
    {
        "id": 29, "bloque": "Determinación y Cierre", "variable": "Ubigeo_Accion",
        "descripcion": "Lugar de la fiscalización (distrito, provincia, departamento)",
        "keywords": ["distrito", "provincia", "departamento", "región",
                     "localidad", "ámbito", "jurisdicción"],
        "query_busqueda": "distrito provincia departamento región ámbito geográfico lugar fiscalización",
    },
]
