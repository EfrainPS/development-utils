"""
Módulo para interactuar con tablas de AWS DynamoDB.

Proporciona funciones para actualizar elementos en DynamoDB
"""

from typing import Any

import boto3
from boto3.dynamodb.conditions import Key
from dotenv import load_dotenv

load_dotenv()

# Configuración global de DynamoDB
DYNAMODB_REGION = "eu-south-2"

def update_dynamo_item(
    table_name: str,
    pk: str,
    sk: str,
    changes: dict[str, Any],
) -> dict[str, Any]:
    """
    Actualiza un elemento en una tabla de DynamoDB.

    Args:
        table_name: Nombre de la tabla de DynamoDB.
        pk: Clave de partición (partition key).
        sk: Clave de ordenamiento (sort key).
        changes: Diccionario con los cambios a realizar.
            Las claves son los nombres de los atributos.

    Returns:
        Diccionario con los atributos actualizados del elemento.
    """
    dynamodb = boto3.resource(
        "dynamodb",
        region_name=DYNAMODB_REGION,
        verify=False,
    )
    table = dynamodb.Table(table_name)

    update_expression = "SET " + ", ".join(
        f"#{key} = :{key}"
        for key in changes
    )

    response = table.update_item(
        Key={
            "pk": pk,
            "sk": sk,
        },
        UpdateExpression=update_expression,
        ExpressionAttributeNames={
            f"#{key}": key
            for key in changes
        },
        ExpressionAttributeValues={
            f":{key}": value
            for key, value in changes.items()
        },
        ReturnValues="ALL_NEW",
    )

    return response["Attributes"]