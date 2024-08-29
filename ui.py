import streamlit as st
import plotly.express as px
import pandas as pd
from typing import List
from dataclasses import dataclass

from models.QueryResponse import QueryResponse, Response
from service.chat_service import getResponse




supported_visualization_chart = ["bar_chart", "pie_chart", "line_chart", "histogram", "text", "area_chart"]


def infer_axes(df, chart_type):
    if chart_type == "pie_chart":

        names_col = df.select_dtypes(include=['object', 'category']).columns[0]
        values_col = df.select_dtypes(include=['number']).columns[0]
        return names_col, values_col
    else:

        x_col = df.select_dtypes(include=['object', 'category']).columns[0]
        y_col = df.select_dtypes(include=['number']).columns[0]
        return x_col, y_col


def create_chart(data, chart_type):
    if isinstance(data, str):
        data = eval(data)
    df = pd.DataFrame(data)

    x_axis, y_axis = infer_axes(df, chart_type)

    if chart_type == "bar_chart":
        return px.bar(df, x=x_axis, y=y_axis)
    elif chart_type == "pie_chart":
        return px.pie(df, names=x_axis, values=y_axis)
    elif chart_type == "line_chart":
        return px.line(df, x=x_axis, y=y_axis)
    elif chart_type == "histogram":
        return px.histogram(df, x=x_axis)
    elif chart_type == "area_chart":
        return px.area(df, x=x_axis, y=y_axis)
    else:
        return None


st.title("SQL Query Chatbot")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "user":
            st.markdown(message["content"])
        else:
            response = message["responses"]
            st.markdown(f"**SQL Query:** {response.snowflakeQuery}")
            st.markdown(f"**Chart Type:** {response.chartType}")

            if response.genericResponseIdentifier:
                st.markdown(f"**Generic Response:** {response.genericResponse}")
            else:
                if response.chartType == "text":
                    if isinstance(response.response, list):
                        for item in response.response:
                            st.markdown(item)
                    else:
                        st.markdown(response.response)
                elif response.chartType in supported_visualization_chart:
                    chart = create_chart(response.response, response.chartType)
                    if chart:
                        st.plotly_chart(chart)
                    else:
                        st.warning("Unable to create chart with the provided data.")
                else:
                    st.warning(f"Unsupported chart type: {response.chartType}")


if prompt := st.chat_input("What would you like to know?"):

    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    response = getResponse(prompt)


    with st.chat_message("assistant"):
        st.markdown(f"**SQL Query:** {response.snowflakeQuery}")
        st.markdown(f"**Chart Type:** {response.chartType}")

        if response.genericResponseIdentifier:
            st.markdown(f"**Generic Response:** {response.genericResponse}")
            st.session_state.messages.append({"role": "assistant", "responses": response})
        else:
            if response.chartType == "text":
                if isinstance(response.response, list):
                    for item in response.response:
                        st.markdown(item)
                else:
                    st.markdown(response.response)
                st.session_state.messages.append({"role": "assistant", "responses": response})
            elif response.chartType in supported_visualization_chart:
                chart = create_chart(response.response, response.chartType)
                if chart:
                    st.plotly_chart(chart)
                else:
                    st.warning("Unable to create chart with the provided data.")
                st.session_state.messages.append({"role": "assistant", "content": chart, "responses": response})
            else:
                st.warning(f"Unsupported chart type: {response.chartType}")


