function myFunction(operation) {
  let costElement = parseFloat(document.getElementById("price").value);
  let weihgtElement = parseFloat(document.getElementById("weight").value);
  let wieghtStep = parseFloat(document.getElementById("weight").step);
  operation == "Up"
    ? increaseWeight(weihgtElement, costElement, wieghtStep)
    : decreaseWeight(weihgtElement, costElement, wieghtStep);
}

function increaseWeight(currentSateWeight, currentStateCost, weightStepState) {
  result = parseFloat(currentSateWeight) + weightStepState;
  document.getElementById("weight").value = result.toFixed(1);
  document.getElementById("price").value = (result.toFixed(1) * 200).toFixed(2);
}

function decreaseWeight(currentSateWeight, currentStateCost, weightStepState) {
  if (currentSateWeight == 0.1) {
    return (document.getElementById("weight").value = currentSateWeight);
  }
  result = parseFloat(currentSateWeight) - weightStepState;
  document.getElementById("weight").value = result.toFixed(1);
  document.getElementById("price").value = (result.toFixed(1) * 200).toFixed(2);
}