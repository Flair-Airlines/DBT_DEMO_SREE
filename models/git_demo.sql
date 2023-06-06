{% set my_data = source('QUALTRICS', 'SURVEY_EMBEDDED_DATA') %}


SELECT *
FROM {{ my_data }}
