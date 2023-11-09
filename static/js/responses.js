function getBotResponse(input) {
  // Simple responses
  if (input.toLowerCase().includes("hello")) {
    return "Hello there How can I help you!";
  } else if (input.toLowerCase().includes("goodbye")) {
    return "Talk to you later!";
  } else if (input.toLowerCase().includes("help")) {
    return "How can I help you!";
  } else if (input.toLowerCase().includes("types of car do you sell")) {
    return response = "We give a wide range of cars on rent, including supercars and price points to cater to a variety of tastes and budgets.";
  } else if (input.toLowerCase().includes("which car you give to rent")) {
    return response = "We provide supercars on rent to fulfill your dreams in real life.";
  } else if (input.toLowerCase().includes("offer customization") || input.toLowerCase().includes("offer personalization options" || input.toLowerCase().includes("offer")) === "Do you offer customization or personalization options?") {
    return response = "Yes, we offer some customization and personalization options for select pieces of car. You can usually find this information on the product page or by contacting our customer service team.";
  } else if (input.toLowerCase().includes("care for my car")) {
    return response = "We provide care instructions for each type of car on our website. This can include tips on cleaning, storing, and protecting your car from damage.";
  } else if (input.toLowerCase().includes("return policy")) {
    return response = "We offer a flexible return policy for our car items. You can usually return an item within a certain timeframe for a full refund or exchange, as long as it meets our return criteria. Be sure to check our return policy page for specific details.";
  } else if (input.toLowerCase().includes("payment options")) {
    return response = "We accept a variety of payment options, including credit cards, debit cards, PayPal, and sometimes other payment methods like Apple Pay or Google Pay.";
  } else if (input.toLowerCase().includes("quality")) {
    return response = "We carefully select our car pieces from reputable manufacturers or artisans who meet our quality standards. We also inspect each item before it is shipped to ensure it meets our expectations. Additionally, we may provide certifications for certain types of car, such as diamonds or gemstones.";
  }else if (input.toLowerCase().includes("gift wrapping") || input.toLowerCase().includes("gift cards")) {
    return "Yes, we offer gift wrapping and gift cards for purchase. You can usually find this information on the product page or by contacting our customer service team.";
  } else if (input.toLowerCase().includes("materials")) {
    return "Our car pieces are made from a variety of materials, including precious metals like gold and silver, gemstones, diamonds, and other high-quality materials. You can usually find information about the materials used in each piece on the product page.";
  } else if (input.toLowerCase().includes("discounts") || input.toLowerCase().includes("promotions")) {
    return "We occasionally offer discounts and promotions on our car items. Be sure to check our website or follow us on social media to stay up-to-date on our latest deals and offers.";
  } 
  else {
    return response = "I'm sorry, I don't understand your question. Please try asking again or contact our customer service team for further assistance.";
  }
}