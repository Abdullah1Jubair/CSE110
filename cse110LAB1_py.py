{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
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
        "<a href=\"https://colab.research.google.com/github/Abdullah1Jubair/CSE110/blob/main/cse110LAB1_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Task 1.1**"
      ],
      "metadata": {
        "id": "KJAXsUqzkjDz"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ZOBhbdVXs_NR",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "886a6117-bffe-435f-dd3d-b533056d19a5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "please enter your word: hello world\n",
            "please enter your year: 21\n",
            "your word is hello world\n",
            "your year is 21\n"
          ]
        }
      ],
      "source": [
        "word = input(\"please enter your word: \")\n",
        "year = int(input(\"please enter your year: \"))\n",
        "print(f\"your word is {word}\")\n",
        "print(f\"your year is {year}\")"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Task 1.2**"
      ],
      "metadata": {
        "id": "YzqJeldZkoM-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "m = int(input(\"please enter your value: \"))\n",
        "n = int(input(\"please enter your value: \"))\n",
        "result1 = m + n\n",
        "result2 = m * n\n",
        "print (f\"summation : {result1}\")\n",
        "print (f\"Multiplication: {result2}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "C1-clPOi0pID",
        "outputId": "eea39c4e-0789-4c3d-bce9-3ecf24a5c64b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "please enter your value: 10\n",
            "please enter your value: 5\n",
            "summation : 15\n",
            "Multiplication: 50\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Task 1.3**"
      ],
      "metadata": {
        "id": "HdsaIFc2kroe"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "m = int(input(\"please enter your number: \"))\n",
        "n = float(input(\"please enter your number: \"))\n",
        "\n",
        "result1 = m + n\n",
        "result2 = m - n\n",
        "\n",
        "print (f\"{result1}  {result2}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OWFGph193DbV",
        "outputId": "e6a6d699-11d5-422e-e32f-14018f90c194"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "please enter your number: 4\n",
            "please enter your number: 5\n",
            "9.0  -1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Task 1.4**"
      ],
      "metadata": {
        "id": "lkibxgYiku-a"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "m = int(input(\"please enter your number: \"))\n",
        "n = int(input(\"please enter your number: \"))\n",
        "convert = float(n)\n",
        "\n",
        "convert2 = str(m)\n",
        "convert3 = str(convert)\n",
        "result = convert2 + convert3\n",
        "print(result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "q2F_sLmo4T9e",
        "outputId": "25cee249-8834-4527-93fe-a2a615069704"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "please enter your number: 2\n",
            "please enter your number: 3\n",
            "23.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Task 2**"
      ],
      "metadata": {
        "id": "_RcwG99Ek7Oh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "M = int(input(\"Please enter the value of M: \"))\n",
        "N = int(input(\"please enter the value of N: \"))\n",
        "\n",
        "result = M**N\n",
        "print(f\"{M} ^ {N} : {result}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EgXLRoi-6hAa",
        "outputId": "536249bb-fce3-4fd0-cbf2-7239664a4721"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please enter the value of M: 10\n",
            "please enter the value of N: 3\n",
            "10 ^ 3 : 1000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Task3**"
      ],
      "metadata": {
        "id": "fqAM-82Gk_hx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "goods = int(input(\"Please enter goods number: \"))\n",
        "load = goods//4\n",
        "maxload = load * 4\n",
        "print(maxload)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uI8ZtcGK7sjw",
        "outputId": "21132f4d-e498-4936-dee8-a9369074ff80"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please enter goods number: 23\n",
            "20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Class evaluation 1**"
      ],
      "metadata": {
        "id": "qZmqIy51lD7n"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "A = int(input(\"please enter the value of A: \"))\n",
        "B = int(input(\"Please enter the value of B: \"))\n",
        "C = int(input(\"Please enter the value of C: \"))\n",
        "D = float(input(\"Please enter the value of D: \"))\n",
        "\n",
        "Formula = A**C + (2*B) * (A//2) - D/3\n",
        "Convert = int(Formula)\n",
        "print(Convert)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UZ-A1xB083pX",
        "outputId": "4f8468b1-5cf0-4bea-8a70-1c85001272b6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "please enter the value of A: 2\n",
            "Please enter the value of B: 6\n",
            "Please enter the value of c: 8\n",
            "Please enter the value of d: 1.3\n",
            "267\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Class Evaluation 2**"
      ],
      "metadata": {
        "id": "z776zP-QlLEM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "A = input(\"please enter your first name: \")\n",
        "B = input(\"please enter your last name: \")\n",
        "C = int(input(\"please enter your age: \"))\n",
        "D = float(input(\"please enter your CGPA: \"))\n",
        "\n",
        "age = C-2\n",
        "CGPA = D + 0.25\n",
        "\n",
        "print(f\"Name : {A} Rahman\")\n",
        "print(f\"Age : {age}\")\n",
        "print(f\"CGPA : {CGPA}\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f3Fc6N7J-zE3",
        "outputId": "9ebf6789-7e02-4847-b43d-7f4c8b6b0186"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "please enter your first name: Labiba\n",
            "please enter your last name: Arif\n",
            "please enter your age: 23\n",
            "please enter your CGPA: 3.7\n",
            "Name : Labiba Rahman\n",
            "Age : 21\n",
            "CGPA : 3.95\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Home Task**"
      ],
      "metadata": {
        "id": "2WyTgwKfqtWE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "chocolate = int(input(\"Please enter your number: \"))\n",
        "distributes = chocolate // 3\n",
        "remaining = chocolate % 3\n",
        "\n",
        "print(f\"Each friend will receive {distributes} chocolates\")\n",
        "print(f\"The number of remaining chocolates is {remaining}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LtLcib4BjzP5",
        "outputId": "36ead863-4cef-4063-8b8c-d9c526cfe592"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Please enter your number: 90\n",
            "Each friend will receive 30 chocolates\n",
            "The number of remaining chocolates is 0\n"
          ]
        }
      ]
    }
  ]
}