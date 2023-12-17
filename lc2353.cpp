/*FRS: wrong result*/
/*
class FoodRatings {
public:
    unordered_map<string,int> foodRatings;
    map<string,pair<string,int>> cR;
    vector<pair<string,string>> foodCuisine;
    void makeRatings(unordered_map<string,int> &foodRatings,
    vector<pair<string,string>> &foodCuisine,
    map<string,pair<string,int>> &cR){
        for(auto it:foodCuisine){
            string newFood=it.second;
            string cuisine=it.first;
            int newRating=foodRatings[newFood];
            if(cR.find(cuisine)!=cR.end()){
                int prevRating=cR[cuisine].second;
                string prevFood=cR[cuisine].first;
                if(newRating>prevRating){
                    cR.erase(cuisine);
                    cR.insert({cuisine,{newFood,newRating}});
                }
                else if(newRating==prevRating && prevFood>newFood){
                    cR.erase(cuisine);
                    cR.insert({cuisine,{newFood,newRating}});
                }
            }
            else{
                cR.insert({cuisine,{newFood,newRating}});
            }
        }
    }
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        
        for(int i=0;i<foods.size();i++){
            foodRatings.insert({foods[i],ratings[i]});
            foodCuisine.push_back({cuisines[i],foods[i]});
        }
        makeRatings(foodRatings,foodCuisine,cR);
        
    }
    
    void changeRating(string food, int newRating) {
        foodRatings[food]=newRating;
        makeRatings(foodRatings,foodCuisine,cR);
    }
    
    string highestRated(string cuisine) {
        return cR[cuisine].first;
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */
