{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPO8YcS4h8M/W3qZpNroQ2h",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Abdullah1Jubair/CSE110/blob/main/CSE110Lab2.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MtegUtD9rbEQ",
        "outputId": "0af27535-d60d-40f1-cbb5-fd69b4562b66"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please enter your number: 7\n",
            "The number is odd\n"
          ]
        }
      ],
      "source": [
        "number = int(input(\"Please enter your number: \"))\n",
        "if number % 2 == 0:\n",
        "    print(\"The number is even\")\n",
        "else:\n",
        "    print(\"The number is odd\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "number1 = int(input(\"Please enter your first number: \"))\n",
        "number2 = int(input(\"Please enter your second number: \"))\n",
        "\n",
        "if number1>number2:\n",
        "    print(\"First is greater\")\n",
        "elif number1<number2:\n",
        "    print(\"Second is greater\")\n",
        "else:\n",
        "    print(\"The number are equal\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "darxvN5-xrvv",
        "outputId": "91aa60e2-acf7-4a44-e611-78d7944dbcfa"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please enter your first number: -33\n",
            "Please enter your second number: 3\n",
            "Second is greater\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "integer = int(input(\"Please enter your integer: \"))\n",
        "if integer % 2 == 0 or integer % 5 == 0:\n",
        "    print(integer)\n",
        "else:\n",
        "    print(\"Not a multiple of 2 OR 5\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lyUR82TSyqzv",
        "outputId": "f8d51974-f8bd-4596-f04b-eb9a933968fd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please enter your integer: 13\n",
            "Not a multiple of 2 OR 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "integer = int(input(\"Please enter your integer: \"))\n",
        "if integer % 2 == 0 and integer % 5 == 0:\n",
        "    print(integer)\n",
        "else:\n",
        "    print(\"Not multiple of 2 and 5 both\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QzFyHELgzzXS",
        "outputId": "11ef8ba3-9d3e-47fd-cebe-65f6359981e1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please enter your integer: 6\n",
            "Not multiple of 2 and 5 both\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cgpa = float(input(\"Please enter your CGPA: \"))\n",
        "credit = int(input(\"Please enter your CREDIT: \"))\n",
        "\n",
        "if 3.80<= cgpa <=3.89 and credit>= 30:\n",
        "    print(\"The student is eligible for a waiver of 25 percent\")\n",
        "elif 3.90<= cgpa <=3.94 and credit>= 30:\n",
        "   print(\"The student is eligible for a waiver of 50 percent\")\n",
        "elif 3.95<= cgpa <=3.99 and credit>= 30:\n",
        "    print(\"The student is eligible for a waiver of 75 percent\")\n",
        "elif cgpa == 4.00 and credit>= 30:\n",
        "    print(\"The student is eligible for a waiver of 100. percent\")\n",
        "else:\n",
        "    print(\"The student is not eligible for a waiver\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NAntPZcw0jUS",
        "outputId": "faf0a7a0-c4cd-49ff-925f-cb7be34f71d4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please enter your CGPA: 3.79\n",
            "Please enter your CREDIT: 24\n",
            "The student is not eligible for a waiver\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Class Evaluation Task 1\n",
        "\n",
        "hours = int(input(\"Please enter working hour: \"))\n",
        "if hours<0:\n",
        "    print(\"Hour cannot be negative\")\n",
        "elif hours>168:\n",
        "    print(\"Impossible to work more than 168 hours weekly\")\n",
        "elif hours<=40:\n",
        "    salary = hours * 200\n",
        "    print(salary)\n",
        "elif hours>40:\n",
        "    salary = 8000+(hours-40)*300\n",
        "    print(salary)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0GF4YGBo297H",
        "outputId": "01a14122-a86d-423c-94bb-2e150e061a79"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please enter working hour: 100\n",
            "26000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Evaluation 2\n",
        "seconds = int(input(\"Please enter your seconds: \"))\n",
        "hours = seconds // 3600\n",
        "seconds = seconds % 3600\n",
        "mins = seconds // 60\n",
        "seconds = seconds % 60\n",
        "print(f\"Hours: {hours}\\nMinutes: {mins}\\nSeconds: {seconds}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DZ-rW3he_P-r",
        "outputId": "ee866349-ee4c-4145-c9e1-aab3a3b646eb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please enter your seconds: 500\n",
            "Hours: 0\n",
            "Minutes: 8\n",
            "Seconds: 20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#evaluation 3\n",
        "s = int(input(\"Please enter your distance_meter: \"))\n",
        "t = int(input(\"Please enter your time_sec: \"))\n",
        "\n",
        "distance_km = s/1000\n",
        "time_h = t//3600\n",
        "v = distance_km/time_h\n",
        "print(f\"{v}Km/h\")\n",
        "if v<60:\n",
        "  print(\"Too slow. It needs more changes \")\n",
        "elif 60>= v <=90:\n",
        "  print(\"Velocity is okay. The car is ready!\")\n",
        "else:\n",
        "  print(\"Too fast. Only a few changes should suffice\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hGItF33D_vnx",
        "outputId": "4582864c-38b3-470f-c953-1d8435782163"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please enter your distance: 25400\n",
            "Please enter your time: 3600\n",
            "25.4Km/h\n",
            "Too slow. It needs more changes \n"
          ]
        }
      ]
    }
  ]
}
