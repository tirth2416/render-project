from flask import Flask, render_template, request
import numpy as np
from scipy import stats

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    t_stat = None
    p_val = None
    result = None

    if request.method == "POST":

        data_input = request.form.get("data")
        pop_mean = float(request.form.get("mean"))
        hypothesis = request.form.get("hypothesis")

        try:
            data = [float(x.strip()) for x in data_input.split(",")]

            t_stat, p_val = stats.ttest_1samp(data, pop_mean, alternative=hypothesis)

            alpha = 0.05

            if p_val < alpha:
                result = "Reject the Null Hypothesis at α = 0.05"
            else:
                result = "Fail to Reject the Null Hypothesis at α = 0.05"

        except:
            result = "Invalid input. Please enter valid numbers."

    return render_template(
        "index.html",
        t_stat=t_stat,
        p_val=p_val,
        result=result
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
