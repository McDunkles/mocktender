import UrlUtils from "@/js/url-utils"

/*
 * Author: Duncan MacLeod (101160585)
 *
 * Makes calls to the API that manipulate the 'account' table
 * 
 */
export default class AccountRepository {

    activeAccountId = -1;

    async getAll() {
      return this._get("getAll");
    }


    async findById(user_id) {

      let requestBody = {
        id: user_id
      }

      let paramString = UrlUtils.toUrlEncoded(requestBody);

      return this._get("findById", paramString);
    }


    async findByName(account_name) {

        let requestBody = {
            username: account_name
        }

        let paramString = UrlUtils.toUrlEncoded(requestBody);

        return this._get("findByName", paramString);
    }


    async getActiveAccount() {
        return this._get("getActiveAccount");
    }
  

    async addAccount(params) {

        /*
        let requestBody = {
          id: '',
          username: '',
          usertype: '',
        };
        */
    
        console.log("Fetching request!");
    
        return this._post(params);
    }


    async _get(path) {
      
      console.log("FETCH PATH = "+`${window.appApiUrl}/account/${path}`)
      let resp = await fetch(`${window.appApiUrl}/account/${path}`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        }
      });
  
      let result = await resp.json();
  
      return result;
    }

    async _post(requestBody) {

        let paramString = UrlUtils.toUrlEncoded(requestBody);
    
        let resp = await fetch(`${window.appApiUrl}/account/addAccount?${paramString}`, {
          method: "POST",
          headers: {
            "Accept": "application/json",
            "Content-Type": "application/json"
          },
          //body: JSON.stringify(requestBody)
          //body: requestBody
        });
        let result = await resp.json();
    
        console.log("add account result = "+JSON.stringify(result));

        this.activeAccountId = result.id;

        console.log("Active ID = "+this.activeAccountId);

        return result;
      }


      getActiveAccountId() {return this.activeAccountId;}
  
  }
  
  
  //export default new AccountRepository();