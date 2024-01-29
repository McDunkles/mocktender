import UrlUtils from "@/js/url-utils"

export default class LiquidContainerMappingRepository {

  async findAll() {
    return this._get("getAll");
  }


  async findByContainerNo(searchParams) {
    return this._getWithParams("findByContainerNo", searchParams);
  }


  async _post(path, requestBody) {
    let resp = await fetch(`${window.appApiUrl}/lci/${path}`, {
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json"
      },
      body: JSON.stringify(requestBody)
    });
    let result = await resp.json();

    return result;
  }

  async _get(path) {
    let resp = await fetch(`${window.appApiUrl}/lci/${path}`, {
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
    let full_call_url = `${window.appApiUrl}/lci/${path}?${paramsString}`;
    //console.log("Full Call URL = "+full_call_url);
    let resp = await fetch(`${window.appApiUrl}/lci/${path}?${paramsString}`, {
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

} 