var productsArray = [];
let costElement = document.getElementById("hiden_price_retail").innerHTML;
let totalPriceElement = document.getElementById("totalPrice");
totalPriceElement.value = costElement;
var res = 0;
function myFunction(operation) {
  let costElement = document.getElementById("hiden_price_retail").innerHTML;
  let weihgtElement = parseFloat(document.getElementById("weight").value);
  let wieghtStep = parseFloat(document.getElementById("weight").step);
  operation == "Up"
    ? increaseWeight(weihgtElement, costElement, wieghtStep)
    : decreaseWeight(weihgtElement, costElement, wieghtStep);
}
function getPrices() {
  let productsPrice = 0;
  let Khatam_Pack = document.getElementById("Khatam_Pack").value;
  let l1 = Khatam_Pack.split(" ").length;
  productsPrice += Number(Khatam_Pack.split(" ")[l1 - 1]);
  let Brass_Grinder_and_Velvet_Pack_Deluxe = document.getElementById(
    "Brass_Grinder_and_Velvet_Pack_Deluxe"
  ).value;
  let l2 = Brass_Grinder_and_Velvet_Pack_Deluxe.split(" ").length;
  productsPrice += Number(
    Brass_Grinder_and_Velvet_Pack_Deluxe.split(" ")[l2 - 1]
  );
  let Diamond_Pack = document.getElementById("Diamond_Pack").value;
  let l3 = Diamond_Pack.split(" ").length;
  productsPrice += Number(Diamond_Pack.split(" ")[l3 - 1]);
  let Brass_Grinder_and_Velvet_Pack = document.getElementById(
    "Brass_Grinder_and_Velvet_Pack"
  ).value;
  let l4 = Brass_Grinder_and_Velvet_Pack.split(" ").length;
  productsPrice += Number(Brass_Grinder_and_Velvet_Pack.split(" ")[l4 - 1]);
  return productsPrice;
}

function increaseWeight(currentSateWeight, currentStateCost, weightStepState) {
  let minBulk = document.getElementById("hiden_weight_bulk").innerHTML;
  let bulkPrice = document.getElementById("hiden_price_bulk").innerHTML;
  result = parseFloat(currentSateWeight) + weightStepState;

  if (result >= minBulk - 0.01) {
    let price = (document.getElementById("price").value = (
      Number(result) * bulkPrice
    ).toFixed(2));

    totalPriceElement.value = Number(price) + getPrices();
  } else {
    let price = (document.getElementById("price").value = (
      result.toFixed(1) * parseFloat(currentStateCost)
    ).toFixed(2));
    totalPriceElement.value = Number(price) + getPrices();
  }
  document.getElementById("weight").value = result.toFixed(1);
}

function decreaseWeight(currentSateWeight, currentStateCost, weightStepState) {
  let minBulk = document.getElementById("hiden_weight_bulk").innerHTML;
  let bulkPrice = document.getElementById("hiden_price_bulk").innerHTML;
  let bulkStep = Number(bulkPrice) / 10;
  let retailStep = Number(currentStateCost) / 10;
  if (currentSateWeight == 0.0) {
    return (document.getElementById("weight").value = currentSateWeight);
  }
  result = parseFloat(currentSateWeight) - weightStepState;

  if (result >= minBulk - 0.01) {
    let price = (document.getElementById("price").value = (
      Number(result) * bulkPrice
    ).toFixed(2));
    totalPriceElement.value = Number(price) + getPrices();
  } else {
    let price = (document.getElementById("price").value = (
      result.toFixed(1) * parseFloat(currentStateCost)
    ).toFixed(2));
    totalPriceElement.value = Number(price) + getPrices();
  }
  document.getElementById("weight").value = result.toFixed(1);
}

function showResult(value) {
  let minBulk = document.getElementById("hiden_weight_bulk").innerHTML;
  let bulkPrice = document.getElementById("hiden_price_bulk").innerHTML;
  let costElement = document.getElementById("hiden_price_retail").innerHTML;
  let productPrices = getPrices();

  if (value >= minBulk - 0.01) {
    let price = (document.getElementById("price").value = value * bulkPrice);

    totalPriceElement.value = Number(price) + productPrices;
  } else {
    let price = (document.getElementById("price").value = value * costElement);

    totalPriceElement.value = Number(price) + productPrices;
  }
}

function validate() {
  const input = document.getElementById("phone");
  const validityState = input.validity;

  if (validityState.valueMissing) {
    input.setCustomValidity("Fill in with following pattern : +79264847255");
  } else if (validityState.rangeUnderflow) {
    input.setCustomValidity("We need a higher number!");
  } else if (validityState.rangeOverflow) {
    input.setCustomValidity("Thats too high!");
  } else if (validityState.patternMismatch) {
    input.setCustomValidity("Fill in with following pattern : +79264847255");
  } else {
    input.setCustomValidity("");
  }

  input.reportValidity();
}

function updateOfferWithproduct(product, price) {
  let obj2 = { key: product, volume: 1, price: price, priceForOne: price };
  if (productsArray.find((obj2) => obj2.key == product)) {
    let index = productsArray.find((obj2) => obj2.key == product);
    index.volume += 1;
    index.price += price;
  } else {
    productsArray.push(obj2);
  }

  let sum = updateUiWithProductList();
  let arr = [];
  let finalSum = 0;
  for (i of productsArray) {
    arr.push(i.price);
  }
  arr;
  arr.forEach((element) => {
    finalSum += element;
  });

  totalPriceElement.value =
    Number(document.getElementById("price").value) + Number(finalSum);
}

function updateUiWithProductList() {
  for (i of productsArray) {
    switch (i.key) {
      case "Brass Grinder and Velvet Pack":
        document.getElementById(
          "Brass_Grinder_and_Velvet_Pack"
        ).value = `${i.key} - ${i.volume} boxes for ${i.price}`;
        res += i.priceForOne;
        break;
      case "Diamond Pack":
        document.getElementById(
          "Diamond_Pack"
        ).value = `${i.key} - ${i.volume} boxes for ${i.price}`;

        res += i.priceForOne;
        break;
      case "Brass Grinder and Velvet Pack - Deluxe":
        document.getElementById(
          "Brass_Grinder_and_Velvet_Pack_Deluxe"
        ).value = `${i.key} - ${i.volume} boxes for ${i.price}`;

        res += i.priceForOne;

        break;
      case "Khatam Pack":
        document.getElementById(
          "Khatam_Pack"
        ).value = `${i.key} - ${i.volume} boxes for ${i.price}`;
        res += i.priceForOne;
        break;
    }
  }
  return Number(res);
}

function addToOffer(value) {
  let title = document.getElementsByClassName("product-description-XRu");
  let price = document.getElementsByClassName("rub-dzj");

  updateOfferWithproduct(
    title[value - 1].innerHTML,
    Number(price[value - 1].innerHTML.split(" ")[0])
  );
}

function updateTotalPrice(value) {
  value;
}
