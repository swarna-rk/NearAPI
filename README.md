# NearAPI
 NearAPI Endpoints

# Endpoint Description
1. https://near-api-tau.vercel.app/AllProjects   -- returns a list of All Projects 

2. https://near-api-tau.vercel.app/AllProjects/[projectname] - returns details of the specified Project name

    examples:
    https://near-api-tau.vercel.app/AllProjects/Near - returns details of the projects with name "Near". One can give full name or partial name

3. https://near-api-tau.vercel.app/AllProjects/HasDApp - returns all projects that has DApp Links

4. https://near-api-tau.vercel.app/AllProjects/HasGrants - returns all projects that has Grants

5. https://near-api-tau.vercel.app/Grants/[providername] - returns all projects granted by an entity

   examples : 
   https://near-api-tau.vercel.app/Grants/Near - returns all projects granted by Near

6. https://near-api-tau.vercel.app/Category/[categoryname] - returns all projects under a specific category

   examples :
   https://near-api-tau.vercel.app/Category/DApps - returns all projects under DApps
   https://near-api-tau.vercel.app/Category/Music - returns all project under Music

7. https://near-api-tau.vercel.app/Series/[seriesname]  - returns all projects under a specific series/tags

   examples :
   https://near-api-tau.vercel.app/Series/SOON - returns all projects with "COMING SOON" tags
   https://near-api-tau.vercel.app/Series/Near -returns all Near projects
   https://near-api-tau.vercel.app/Series/Aurora - returns all Aurora Projects

8. https://near-api-tau.vercel.app/AllProjects/Links/[projectname] - returns all url links of the matched project name

   examples :
    https://near-api-tau.vercel.app/AllProjects/Links/Loozr - returns all urls of project named 'Loozr'
    https://near-api-tau.vercel.app/AllProjects/Links/Near - returns all urls of all projects with "Near" in its name

9. https://near-api-tau.vercel.app/AllProjects/Tokens/[projectname] - returns all token urls of the matched project

    examples:
    https://near-api-tau.vercel.app/AllProjects/Tokens/Loozr - returns all token urls of the project named "Loozr"
     https://near-api-tau.vercel.app/AllProjects/Tokens/Near - returns all token urls of all projects with "Near" in its name    
     
 10. https://near-api-tau.vercel.app/Projects/Create - Creates a new entry in NearProjects JSON file. This method should be invoked while submitting new project details
 
 URL : https://near-api-tau.vercel.app/Projects/Create
 
 Sample input : {
	"ProjectName": "ABCD",
	"Category": null,
	"Subtitle": null,
	"AwesomeNearLink": null,
	"Series": null,
	"ABBV": null,
	"Icon": "ABCD",
	"Website Link": "ABCD",
	"Buy Link": null,
	"Stake Link": null,
	"DApp Link": "ABCD",
	"Facebook": "ABCD",
	"Twitter": "ABCD",
	"Github": "ABCD",
	"Telegram": "ABCD",
	"Discord": "ABCD",
	"Linkedin": null,
	"Medium": "ABCD",
	"Other Links": null,
	"Near Token": null,
	"Aurora Token": null,
	"Ethereum Token": null,
	"Other Tokens": "ABCD",
	"Description": "ABCD",
	"Grants": null,
	"News Articles": null,
	"WalletSelector_Comments1": null,
	"WalletSelector_Comments2": null,
	"Notes": "PrevFundraising:xyza|CurrentFundraising:ABCD|TobeContacted:ABCD|Integrated_WS:ABCD|Email:ABCD|ContactEmail:ABCD",
	"Date_Created": "ABCD"
}

Output : Success

