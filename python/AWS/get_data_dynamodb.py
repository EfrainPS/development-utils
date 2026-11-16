"""
Módulo para interactuar con tablas de AWS DynamoDB.

Proporciona funciones para consultar elementos en DynamoDB,
integrándose con Polars para manipulación de datos.
"""

from typing import Any

import boto3
import polars as pl
from boto3.dynamodb.conditions import Key
from dotenv import load_dotenv

load_dotenv()

# Configuración global de DynamoDB
DYNAMODB_REGION = "eu-south-2"


def get_data(
    table_name: str,
    pk: str,
    sk: str | None = None,
) -> pl.DataFrame:
    """
    Obtiene datos de una tabla de DynamoDB.

    Args:
        table_name: Nombre de la tabla de DynamoDB.
        pk: Clave de partición (partition key).
        sk: Clave de ordenamiento (sort key). Si se proporciona,
            realiza una búsqueda de prefijo. Opcional.

    Returns:
        DataFrame de Polars con los elementos recuperados.
    """
    dynamodb = boto3.resource(
        "dynamodb",
        region_name=DYNAMODB_REGION,
        verify=False,
    )
    table = dynamodb.Table(table_name)

    if sk:
        response = table.query(
            KeyConditionExpression=Key("pk").eq(pk)
            & Key("sk").begins_with(sk)
        )
    else:
        response = table.query(
            KeyConditionExpression=Key("pk").eq(pk)
        )

    items = response.get("Items", [])
    return pl.DataFrame(items)