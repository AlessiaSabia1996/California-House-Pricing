import click
import joblib
import numpy as np

@click.command()
@click.option("--features", "-f", nargs=8, type=float, required=True, help='8 Feature expected: Insert income, house age, number of rooms, number of bedrooms, population, number of household members, latitude, longitude ')
def predict(features):
    
    if len(features) != 8:
        click.echo('some feature is missing!')
        return
    
    model = joblib.load("src\mlopsapp\model.pkl")
    prediction = model.predict([features])
    click.echo(f"Predicted price {(prediction[0]*100000):.2f} $")

if __name__ == "__main__":
    predict()
