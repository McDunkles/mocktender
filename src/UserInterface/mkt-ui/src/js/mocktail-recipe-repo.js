import UrlUtils from "@/js/url-utils"

export default class MocktailRecipeRepository {

  async find(searchParams) {
    return this._getWithParams("/findByName", searchParams);
  }

  async findAll() {
    return this._get("/findAll");
  }

  async getByName(id) {
    return this._get(id);
  }

  async _get(path) {
    
    //console.log("Ayo 2");
    let resp = await fetch(`${window.appApiUrl}/recipes/${path}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json"
      }
    });
    let result = await resp.json();

    //console.log("RESPONSE = "+JSON.stringify(result));
    return result;
  }

  async _getWithParams(path, searchParams) {
    //console.log("Ayo 1");
    let paramsString = UrlUtils.toUrlEncoded(searchParams);
    let full_call_url = `${window.appApiUrl}/recipes/${path}?${paramsString}`;
    //console.log("Full Call URL = "+full_call_url);
    let resp = await fetch(`${window.appApiUrl}/recipes/${path}?${paramsString}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json"
      }
    });

    if (!resp.ok) {
      console.error("Buildings search failed: " + resp.statusText);
      throw new Error("Something went wrong on sevrer");
    }

    let result = await resp.json();


    //console.log("RESPONSE = "+JSON.stringify(result));
    return result;
  }


  /*
  async _post(params) {

    let paramsString = UrlUtils.toUrlEncoded(params);

    let resp = await fetch(`${window.appApiUrl}/recipes/addMocktail`, {
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json"
      },
      body: JSON.stringify(params)
    });
    let result = await resp.json();

    return result;
  }
  */

  
  async _post(requestBody) {

    let paramString = UrlUtils.toUrlEncoded(requestBody);

    let resp = await fetch(`${window.appApiUrl}/recipes/addMocktail?${paramString}`, {
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json"
      },
      //body: JSON.stringify(requestBody)
      //body: requestBody
    });
    let result = await resp.json();

    return result;
  }
  

  /*
  async _post(requestBody) {

    //let paramString = UrlUtils.toUrlEncoded(requestBody);

    let resp = await fetch(`${window.appApiUrl}/recipes/addMocktail`, {
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json"
      },
      body: UrlUtils.toUrlEncoded(requestBody)
      //body: requestBody
    });
    let result = await resp.json();

    return result;
  }
  */


  async addMocktail(params) {

    /*
    let requestBody = {
      name: '',
      liquid1: '',
      amount1: '',
      liquid2: '',
      amount2: '',
      liquid3: '',
      amount3: ''
    };
    */

    console.log("Fetching request!");

    return this._post(params);

  }

} 