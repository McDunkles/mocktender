
/*
 * Author: Duncan MacLeod (101160585)
 *
 * 
 */
class AuthRepository {

  async getInfo() {
    return this._get("info");
  }

  async _get(path) {
    
    console.log("FETCH PATH = "+`${window.appBaseUrl}/auth/${path}`)
    let resp = await fetch(`${window.appBaseUrl}/auth/${path}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json"
      }
    });

    let result = await resp.json();

    return result;
  }

}


export default new AuthRepository();