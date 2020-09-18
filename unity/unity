using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class PlayerController : MonoBehaviour
{
    private Vector3 offset;
    private Vector3 screenPoint;
    private Vector3 newPosition;
    private Vector3 cursorPoint;
    private Vector3 oldPosition;
    private GameObject triggerObject;
    private int i;
    private string[] sphereList = {"Sphere1", "Sphere2", "Sphere3", "Sphere4"};
    private string[] colors = {"Color1", "Color2", "Color3", "Color4", "Color5", "Color6"};
    private string[] winning_colors = {"", "", "", ""};
    private GameObject WinningColors;
    private int[] gameRes;
    // Start is called before the first frame update
    void Start()
    {
        oldPosition = transform.position;
        // Generates random winning colors
        System.Random randomize = new System.Random(); 
        for (int i = 0; i < 4; i++){
            int index = randomize.Next(6);
            winning_colors[i] = colors[index];
      
        }

        WinningColors = GameObject.FindWithTag("WinningColors");
        i = 0;
        foreach(Transform child in WinningColors.transform){
            if (child.name != "Result"){
                child.name = winning_colors[i];
                child.GetComponent<MeshRenderer>().material = GameObject.Find(winning_colors[i].Replace("Color", "ColorPicker")).GetComponent<MeshRenderer>().material;
            }
            i++;
        }

    }


    void OnMouseDown(){
        // Gets cursor position and offset on click
        screenPoint = Camera.main.WorldToScreenPoint(transform.position);
        offset = transform.position - Camera.main.ScreenToWorldPoint(new Vector3(Input.mousePosition.x, Input.mousePosition.y, screenPoint.z));
    }

    void OnMouseUp(){
        // Resets position of the color when click is released
        transform.position = oldPosition;
        i = 0;
        string[] colorList = {"", "", "", ""};
        foreach (var s in sphereList){
            if (s == triggerObject.name){
                // Replace the color with the new one
                triggerObject.GetComponent<MeshRenderer>().material = this.GetComponent<MeshRenderer>().material;
                foreach (Transform child in triggerObject.transform.parent){
                    if (child.name != "Result" && child.GetComponent<MeshRenderer>().material.name != "Default-Material (Instance)"){
                            colorList[i] = child.GetComponent<MeshRenderer>().material.name.Substring(0, 6);
                            //Debug.Log(child.GetComponent<MeshRenderer>().material.name.Substring(0, 6));
                            i++;
                        }
                }
            }
        }

     
        if (i == 4){ 
            // Did the player win the game ? Launch function
            gameRes = MasterMindLogic(winning_colors, colorList);
            // Checks if the player won the game
            if (gameRes[0] != 4){
                int index = gameRes[0]; // Number of matches
                Transform res = triggerObject.transform.parent.Find("Result");
                foreach (Transform child in res){
                    // Setup color black or white depending on gameRes
                    if (index > 0){
                        child.GetComponent<MeshRenderer>().material.color = Color.black;
                        index--;
                    }
                    else{
                        child.GetComponent<MeshRenderer>().material.color = Color.white;
                    }
                }
               
            }
            else{
                Transform res = triggerObject.transform.parent.Find("Result");
                foreach (Transform child in res){
                    // Setup color black after winning the game
                    child.GetComponent<MeshRenderer>().material.color = Color.black;
                }
                // Player won

                
            }

         
        foreach (Transform child in triggerObject.transform.parent){
                if (child.name != "Result"){
                    Destroy(child.GetComponent<SphereCollider>());
                }
            }
        }
       
    }


    void OnTriggerEnter(Collider other) {
       triggerObject = other.gameObject;
    }
    void OnMouseDrag()
    {
        // Drag the current color to the mouse position
        cursorPoint = new Vector3(Input.mousePosition.x, Input.mousePosition.y, screenPoint.z);
        newPosition = Camera.main.ScreenToWorldPoint(cursorPoint) + offset;
        transform.position = newPosition;
    }

    int[] MasterMindLogic(string[] winning_colors, string[] player_colors){
	/**
	winning_colors: a 4 digit generated number by the computer
	player_colors: a 4 digit choosen by the player
	
	This function checks the player_colors against the winning colors 
	to see if there is a match then returns the number of matches.

	Example:
	> win: 1234
	> player_colors: 1324

	> output: 1/4
	-> there is one mtach and 3 dismatches
	**/
        int[] result = {0, 0};


        for (int i = 0; i < winning_colors.Length; i++){
            if (winning_colors[i].ToLower() == player_colors[i].ToLower()){
                result[0] += 1;
            }
            else{
                result[1] += 1;
            }   
        }
        return result;
    }

}
