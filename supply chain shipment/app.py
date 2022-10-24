from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle

app = Flask(__name__,template_folder='templates')

model = pickle.load(open(r'C:\Users\Dell\ALL PROGRAMMING\supply chain shipment\saved_model.pkl', 'rb'))



@app.route("/")
@cross_origin()
def home():
    return render_template("template.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        #Managed by
        ManagedBy=request.form['ManagedBy']
        if(ManagedBy=='PMO - US'):
            ManagedBy = 1
        else:
            ManagedBy=0
            
            
        #FulfillVia
        FulfillVia =request.form["FulfillVia"]
        if(FulfillVia=='From RDC'):
            FulfillVia = 1
        else:
            FulfillVia=0
        
        
        #VendorINCOTerm
        VendorINCOTerm =request.form["VendorINCOTerm"]
        if(FulfillVia=='N/A - From RDC'):
            FulfillVia=0
        elif(FulfillVia=='EXW'):
            FulfillVia=1
        elif(FulfillVia=='DDP'):
            FulfillVia=2
        elif(FulfillVia=='FCA'):
            FulfillVia=3
        elif(FulfillVia=='CIP'):
            FulfillVia=4
        else:
            FulfillVia=5

        #PQFirstSenttoClientDate
        PQFirstSenttoClientDate =request.form["PQFirstSenttoClientDate"]
        if(PQFirstSenttoClientDate=='Pre-PQ Process'):
            PQFirstSenttoClientDate = 0
        else:
            PQFirstSenttoClientDate=1
            
        
        #POSenttoVendorDate
        POSenttoVendorDate =request.form["POSenttoVendorDate"]
        if(PQFirstSenttoClientDate=='N/A - From RDC'):
            PQFirstSenttoClientDate = 1
        elif(PQFirstSenttoClientDate=='Date Not Captured'):
            PQFirstSenttoClientDate=0
        else:
            PQFirstSenttoClientDate=2
        
        
        #Vendor
        Vendor =request.form["Vendor"]
        if(Vendor=='SCMS from RDC'):
            Vendor = 0
        else:
            Vendor=1

        #UnitofMeasurePerPack
        UnitofMeasurePerPack=int(request.form["UnitofMeasurePerPack"])
        #"LineItemQuantity
        LineItemQuantity=int(request.form["LineItemQuantity"])
        #"LineItemValue"
        FirstLineDesignation=request.form["FirstLineDesignation"]
        if(FirstLineDesignation=="True"):
            FirstLineDesignation=True
        else:
            FirstLineDesignation=False
        #"PackPrice"
        PackPrice=int(request.form["PackPrice"])
        #"UnitPrice",
        UnitPrice=int(request.form["UnitPrice"])
        #"WeightKilograms",
        WeightKilograms=int(request.form["WeightKilograms"])
        #"FreightCostUSD"
        FreightCostUSD=int(request.form["FreightCostUSD"])
        #LineItemInsuranceUSD
        LineItemInsuranceUSD=int(request.form["LineItemInsuranceUSD"])
        
        #Country
        Country=request.form['Country']
        if(Country=='Cameroon'):
           Country_Cameroon=1
           Country_CongoDRC=0
           Country_CtedIvoire=0
           Country_Ethiopia=0
           Country_Guyana=0
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=0
           Country_SouthSudan=0
           Country_Tanzania=0
           Country_Uganda=0
           Country_Vietnam=0
           Country_Zambia=0
           Country_Zimbabwe=0 

        elif(Country=='Congo, DRC'):
           Country_Cameroon=0
           Country_CongoDRC=1
           Country_CtedIvoire=0
           Country_Ethiopia=0
           Country_Guyana=0
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=0
           Country_SouthSudan=0
           Country_Tanzania=0
           Country_Uganda=0
           Country_Vietnam=0
           Country_Zambia=0
           Country_Zimbabwe=0
   
        elif(Country=='South Africa'):
           Country_Cameroon=0
           Country_CongoDRC=0
           Country_CtedIvoire=0
           Country_Ethiopia=0
           Country_Guyana=0
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=1
           Country_SouthSudan=0
           Country_Tanzania=0
           Country_Uganda=0
           Country_Vietnam=0
           Country_Zambia=0
           Country_Zimbabwe=0
           
        elif(Country=='Nigeria'):
           Country_Cameroon=0
           Country_CongoDRC=0
           Country_CtedIvoire=0
           Country_Ethiopia=0
           Country_Guyana=0
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=1
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=0
           Country_SouthSudan=0
           Country_Tanzania=0
           Country_Uganda=0
           Country_Vietnam=0
           Country_Zambia=0
           Country_Zimbabwe=0
           
        
        elif(Country=='CÃ´tedIvoire'):
           Country_Cameroon=0
           Country_CongoDRC=0
           Country_CtedIvoire=1
           Country_Ethiopia=0
           Country_Guyana=0
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=0
           Country_SouthSudan=0
           Country_Tanzania=0
           Country_Uganda=0
           Country_Vietnam=0
           Country_Zambia=0
           Country_Zimbabwe=0
          
        elif(Country=='Uganda'):
           Country_Cameroon=0
           Country_CongoDRC=0
           Country_CtedIvoire=0
           Country_Ethiopia=0
           Country_Guyana=0
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=0
           Country_SouthSudan=0
           Country_Tanzania=0
           Country_Uganda=1
           Country_Vietnam=0
           Country_Zambia=0
           Country_Zimbabwe=0
          
        elif(Country=='Vietnam'):
           Country_Cameroon=0
           Country_CongoDRC=0
           Country_CtedIvoire=0
           Country_Ethiopia=0
           Country_Guyana=0
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=0
           Country_SouthSudan=0
           Country_Tanzania=0
           Country_Uganda=0
           Country_Vietnam=1
           Country_Zambia=0
           Country_Zimbabwe=0
           
        elif(Country=='Zambia'):
           Country_Cameroon=0
           Country_CongoDRC=0
           Country_CtedIvoire=0
           Country_Ethiopia=0
           Country_Guyana=0
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=0
           Country_SouthSudan=0
           Country_Tanzania=0
           Country_Uganda=0
           Country_Vietnam=0
           Country_Zambia=1
           Country_Zimbabwe=0
           
        elif(Country=='Haiti'):
           Country_Cameroon=0
           Country_CongoDRC=0
           Country_CtedIvoire=0
           Country_Ethiopia=0
           Country_Guyana=0
           Country_Haiti=1
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=0
           Country_SouthSudan=0
           Country_Tanzania=0
           Country_Uganda=0
           Country_Vietnam=0
           Country_Zambia=0
           Country_Zimbabwe=0
           
        elif(Country=='Mozambique'):
           Country_Cameroon=0
           Country_CongoDRC=0
           Country_CtedIvoire=0
           Country_Ethiopia=0
           Country_Guyana=0
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=1
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=0
           Country_SouthSudan=0
           Country_Tanzania=0
           Country_Uganda=0
           Country_Vietnam=0
           Country_Zambia=0
           Country_Zimbabwe=0
           
        elif(Country=='Zimbabwe'):
           Country_Cameroon=0
           Country_CongoDRC=0
           Country_CtedIvoire=0
           Country_Ethiopia=0
           Country_Guyana=0
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=0
           Country_SouthSudan=0
           Country_Tanzania=0
           Country_Uganda=0
           Country_Vietnam=0
           Country_Zambia=0
           Country_Zimbabwe=1
           
        elif(Country=='Tanzania'):
           Country_Cameroon=0
           Country_CongoDRC=0
           Country_CtedIvoire=0
           Country_Ethiopia=0
           Country_Guyana=0
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=0
           Country_SouthSudan=0
           Country_Tanzania=1
           Country_Uganda=0
           Country_Vietnam=0
           Country_Zambia=0
           Country_Zimbabwe=0
           
        elif(Country=='Rwanda'):
           Country_Cameroon=0
           Country_CongoDRC=0
           Country_CtedIvoire=0
           Country_Ethiopia=0
           Country_Guyana=0
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=1
           Country_SouthAfrica=0
           Country_SouthSudan=0
           Country_Tanzania=0
           Country_Uganda=0
           Country_Vietnam=0
           Country_Zambia=0
           Country_Zimbabwe=0
           
        elif(Country=='Guyana'):
           Country_Cameroon=0
           Country_CongoDRC=0
           Country_CtedIvoire=0
           Country_Ethiopia=0
           Country_Guyana=1
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=0
           Country_SouthSudan=0
           Country_Tanzania=0
           Country_Uganda=0
           Country_Vietnam=0
           Country_Zambia=0
           Country_Zimbabwe=0
           
           
        elif(Country=='Ethiopia'):
           Country_Cameroon=0
           Country_CongoDRC=0
           Country_CtedIvoire=0
           Country_Ethiopia=1
           Country_Guyana=0
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=0
           Country_SouthSudan=0
           Country_Tanzania=0
           Country_Uganda=0
           Country_Vietnam=0
           Country_Zambia=0
           Country_Zimbabwe=0
           
        elif(Country=='South Sudan'):
           Country_Cameroon=0
           Country_CongoDRC=0
           Country_CtedIvoire=0
           Country_Ethiopia=0
           Country_Guyana=0
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=0
           Country_SouthSudan=1
           Country_Tanzania=0
           Country_Uganda=0
           Country_Vietnam=0
           Country_Zambia=0
           Country_Zimbabwe=0
           
        elif(Country=='Kenya'):
            Country_Cameroon=0
            Country_CongoDRC=0
            Country_CtedIvoire=0
            Country_Ethiopia=0
            Country_Guyana=0
            Country_Haiti=0
            Country_Kenya=1
            Country_Mozambique=0
            Country_Namibia=0
            Country_Nigeria=0
            Country_Other=0
            Country_Rwanda=0
            Country_SouthAfrica=0
            Country_SouthSudan=0
            Country_Tanzania=0
            Country_Uganda=0
            Country_Vietnam=0
            Country_Zambia=0
            Country_Zimbabwe=0
           
        elif(Country=='Burundi'):
           Country_Cameroon=0
           Country_CongoDRC=0
           Country_CtedIvoire=0
           Country_Ethiopia=0
           Country_Guyana=0
           Country_Haiti=0
           Country_Kenya=0
           Country_Mozambique=0
           Country_Namibia=0
           Country_Nigeria=0
           Country_Other=0
           Country_Rwanda=0
           Country_SouthAfrica=0
           Country_SouthSudan=0
           Country_Tanzania=0
           Country_Uganda=0
           Country_Vietnam=0
           Country_Zambia=0
           Country_Zimbabwe=0
           
        
        else:
            Country_Cameroon=0
            Country_CongoDRC=0
            Country_CtedIvoire=0
            Country_Ethiopia=0
            Country_Guyana=0
            Country_Haiti=0
            Country_Kenya=0
            Country_Mozambique=0
            Country_Namibia=0
            Country_Nigeria=0
            Country_Other=1
            Country_Rwanda=0
            Country_SouthAfrica=0
            Country_SouthSudan=0
            Country_Tanzania=0
            Country_Uganda=0
            Country_Vietnam=0
            Country_Zambia=0
            Country_Zimbabwe=0
         
         
           
                
        
        
        ShipmentMode=request.form['ShipmentMode']
        if(ShipmentMode=='Air'):
            ShipmentMode_AirCharter=0
            ShipmentMode_Ocean=0
            ShipmentMode_Truck=0  
        elif (ShipmentMode=='Truck'):
            ShipmentMode_AirCharter=0
            ShipmentMode_Ocean=0
            ShipmentMode_Truck=1
            
        elif (ShipmentMode=='Ocean'):
            ShipmentMode_AirCharter=0
            ShipmentMode_Ocean=1
            ShipmentMode_Truck=0
        else:
            ShipmentMode_AirCharter=1
            ShipmentMode_Ocean=0
            ShipmentMode_Truck=0
            
        
            
        
        #ProductGroup
        ProductGroup=request.form['ProductGroup']
        if(ProductGroup=='ARV'):
            ProductGroup_ANTM=0
            ProductGroup_ARV=1
            ProductGroup_HRDT=0
            ProductGroup_MRDT=0
        elif(ProductGroup=='HRDT'):
            ProductGroup_ANTM=0
            ProductGroup_ARV=0
            ProductGroup_HRDT=1
            ProductGroup_MRDT=0
        elif(ProductGroup=='ANTM'):
            ProductGroup_ANTM=1
            ProductGroup_ARV=0
            ProductGroup_HRDT=0
            ProductGroup_MRDT=0
        elif(ProductGroup=='MRDT'):
            ProductGroup_ANTM=0
            ProductGroup_ARV=0
            ProductGroup_HRDT=0
            ProductGroup_MRDT=1
        else:
            ProductGroup_ANTM=0
            ProductGroup_ARV=0
            ProductGroup_HRDT=0
            ProductGroup_MRDT=0
            
        
        SubClassification=request.form['SubClassification']
        if(SubClassification=='Adult'):
            SubClassification_Adult=1
            SubClassification_HIVtest=0
            SubClassification_HIVtestAncillary=0
            SubClassification_Malaria=0
            SubClassification_Pediatric=0
        elif(SubClassification=='Pediatric'):
            SubClassification_Adult=0
            SubClassification_HIVtest=0
            SubClassification_HIVtestAncillary=0
            SubClassification_Malaria=0
            SubClassification_Pediatric=1
        elif(SubClassification=='HIV test'):
            SubClassification_Adult=0
            SubClassification_HIVtest=1
            SubClassification_HIVtestAncillary=0
            SubClassification_Malaria=0
            SubClassification_Pediatric=0
        elif(SubClassification=='HIV test - Ancillary'):
            SubClassification_Adult=0
            SubClassification_HIVtest=0
            SubClassification_HIVtestAncillary=1
            SubClassification_Malaria=0
            SubClassification_Pediatric=0
        elif(SubClassification=='Malaria'):
            SubClassification_Adult=0
            SubClassification_HIVtest=0
            SubClassification_HIVtestAncillary=0
            SubClassification_Malaria=1
            SubClassification_Pediatric=0
        else:
            SubClassification_Adult=0
            SubClassification_HIVtest=0
            SubClassification_HIVtestAncillary=0
            SubClassification_Malaria=0
            SubClassification_Pediatric=0
        
        
                
        prediction=model.predict([[
            ManagedBy, 
            FulfillVia,
           VendorINCOTerm,
           PQFirstSenttoClientDate,
           POSenttoVendorDate,
           Vendor,
           UnitofMeasurePerPack,
           LineItemQuantity,
           PackPrice,
           UnitPrice,
           FirstLineDesignation,
           WeightKilograms,
           FreightCostUSD,
           LineItemInsuranceUSD,
           Country_Cameroon,
           Country_CongoDRC,
           Country_CtedIvoire,
           Country_Ethiopia,
           Country_Guyana,
           Country_Haiti,
           Country_Kenya,
           Country_Mozambique,
           Country_Namibia,
           Country_Nigeria,
           Country_Other,
           Country_Rwanda,
           Country_SouthAfrica,
           Country_SouthSudan,
           Country_Tanzania,
           Country_Uganda,
           Country_Vietnam,
           Country_Zambia,
           Country_Zimbabwe,
           ShipmentMode_AirCharter,
           ShipmentMode_Ocean,
           ShipmentMode_Truck,
           ProductGroup_ANTM,
           ProductGroup_ARV,
           ProductGroup_HRDT,
           ProductGroup_MRDT,
           SubClassification_Adult,
           SubClassification_HIVtest,
           SubClassification_HIVtestAncillary,
           SubClassification_Malaria,
           SubClassification_Pediatric
       ]])

        output=round(prediction[0],2)

        return render_template('template.html',"dsfs",prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("template.html")

if __name__ == "__main__":
    app.run(debug = True)
