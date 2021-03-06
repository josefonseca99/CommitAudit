# Credenciales

CREDENTIALS = ":zinwcppehv5zwic2owfmruhesg3ybavczj6fq7zzgk5hecktz6pa"

# Constantes para los commits

ATTACHMENT_REQUEST_1 = "https://{}/{}/{}/_apis/git/repositories/{}/commits?"
ATTACHMENT_REQUEST_2 = "api-version=5.1"
FROM_DATE_REQUEST = "searchCriteria.fromDate={}&"
TO_DATE_REQUEST = "searchCriteria.toDate={}&"
USERNAME = "searchCriteria.user={}&"

# Constantes para obtener historias por sprints

US_ATTACHMENT_REQUEST_1 = "https://{}/{}/{}/{}/_apis/work/teamsettings/iterations?api-version=5.1"
US_NUMBER_STR = "Sprint {}"

# Constantes para obtener informacion por código de historia de usuario

US_ID_ATTACHMENT_REQUEST = "https://{}/{}/{}/_apis/wit/workitems?ids={}&api-version=5.1"

# Constante para obtener la lista de historias de usuario por proyecto

USID_ATTACHMENT_REQUEST_1 = "https://{}/{}/{}/{}/_apis/work/teamsettings/iterations/{" \
                            "}/workitems?api-version=5.1-preview.1 "

# Constante para obtener los commit con status completed

COMMIT_STATUS_ATTACHMENT_REQUEST_1 = "https://{}/{}/{}" \
                                     "/_apis/git/repositories/{}/pullrequests?searchCriteria" \
                                     ".status=completed&$top=1000000"

# Constante para obtener la deuda técnica SONAR

TECHNICAL_DEBT_REQUEST = "http://sonar.bancolombia.corp/sonarbc/api/measures/component?component={" \
                         "}&metricKeys=sqale_index "

# Constante para obtener el code smell

CODE_SMELL_REQUEST = "http://sonar.bancolombia.corp/sonarbc/api/measures/component?component={}&metricKeys=code_smells"

# Constantes para el archivo de auditoria
EXCEL_FILE_NAME = "Auditoria_Azure_Repos"

FIRST_STRING = "Ingrese una fecha de inicio y fin, dicho rango de fechas establecer un limite de busqueda para los commits\n"
DATE_FORMAT = "con el formato DD/MM/AAAA: "
FROM_MESSAGE = "Ingresa la fecha de inicio, "
TO_MESSAGE = "Ingresa la fecha final, "
PROJECT_NAME_STRING = "Ingresa el nombre del proyecto: "
ANALYST_STRING = "Ingresa el nombre o correo del analista: "
DATE_ERROR = "El formato de fechas ingresado no el válido. Debería ser DD/MM/YYYY\n"
FOUND_COMMIT_STRING = ["Se ha encontrado un total de", "commits\n", "commit\n"]
ANALYST_SELECTION_STRING = "Ingrese el número de la persona a la cual desea revisar sus numero de commits: "
NUMBER_OF_STRING = ["El número de commits para", "es de:"]
INTERRUPTION_STRING = "Si desea volver a realizar la ejecución ingrese cualquier cosa, en caso contrario ingrese -1"

EXCEL_FILE_NAME = "Auditoria_Azure_Repos.xlsx"
EXCEL_ANALYSTS = "analysts.xlsx"

HEADER_VALUES = ["Sprint", "Nombre del analista", "Habilitadores", "Historias de Usuario", "Bug", "Estado \"New\"",
                 "Estado \"Active\"", "Estado \"Closed\"", "Estado \"Impedimento\"", "Puntos de Historia realizados",
                 "Tareas", "Pull requests", "Commits", "Deuda téctina\n(Minutos)", "Code Smell\n(Minutos)"]
