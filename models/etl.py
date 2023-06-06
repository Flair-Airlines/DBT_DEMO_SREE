# etl.py

def model(dbt, session):

    # dbt.config(materialized="view")

    # DataFrame representing an upstream source
    df = dbt.source('QUALTRICS', 'SURVEY_EMBEDDED_DATA')

    #df = df[['KEY','RESPONSE_ID','VALUE']]

    return df   