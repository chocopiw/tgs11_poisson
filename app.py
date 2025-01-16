from flask import Flask, request, render_template # type: ignore
import math

app = Flask(__name__)

def poisson_probability(lmbda, k):
    """Calculate the Poisson probability."""
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Retrieve and validate inputs
            lmbda = float(request.form['lambda'])
            max_k = int(request.form['max_k'])
            
            # Calculate Poisson probabilities
            probabilities = [
                {'k': k, 'probability': poisson_probability(lmbda, k), 'percentage': poisson_probability(lmbda, k) * 100}
                for k in range(max_k + 1)
            ]

            return render_template('index.html', lmbda=lmbda, max_k=max_k, probabilities=probabilities)

        except (ValueError, KeyError):
            # Handle invalid input or missing fields
            return render_template('index.html', error="Invalid input. Please enter numeric values.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
