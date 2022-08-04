import json
import time
import colorama
import requests

from colorama import Fore

class Main:
    def __init__(self) -> None:
        colorama.init(autoreset=True)

    def LocChunksLoader(self):
        with open('datas/PakChunks.json', 'r') as aes:
            aes = json.load(aes)

    def NewFeaturedIcons(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Outfit/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://fortnitecentral.gmatrixgames.ga/api/v1/export?path={path}')
                pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Outfit/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content)

    def NewBackpacksIcons(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/Icons/Backpacks/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://fortnitecentral.gmatrixgames.ga/api/v1/export?path={path}')
                pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/Icons/Backpacks/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content) 

    def NewEmotesIcons(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Emotes/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://fortnitecentral.gmatrixgames.ga/api/v1/export?path={path}')
                pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Emotes/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content)

    def NewPickaxeIcons(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Pickaxe/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://fortnitecentral.gmatrixgames.ga/api/v1/export?path={path}')
                pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/BattleRoyale/FeaturedItems/Pickaxe/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content) 

    def NewMusicsIcons(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/2dAssets/Music/Season21/PreviewImages/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://fortnitecentral.gmatrixgames.ga/api/v1/export?path={path}')
                pathname = (path.split('FortniteGame/Content/2dAssets/Music/Season21/PreviewImages/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content)


        for i in Icons:
            if i.startswith('FortniteGame/Content/UI/Foundation/Textures/Icons/Heroes/Athena/Soldier/'):
                if i.endswith('-L'):
                    path = i
                    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                    image = requests.get(f'https://fortnitecentral.gmatrixgames.ga/api/v1/export?path={path}')
                    pathname = (path.split('FortniteGame/Content/UI/Foundation/Textures/Icons/Heroes/Athena/Soldier/')[-1])
                    open(f'images/{pathname}.png', 'wb+').write(image.content)
                else:
                    print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.RED + "Skipped " + Fore.CYAN + path)

    def NewCosmeticsIcons(self):
        with open('datas/NewCosmetics.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons['data']['items']:
            id = i['id']
            image = i['images']['icon']
            r = requests.get(image)
            open(f'images/{id}.png', 'wb+').write(r.content)
            print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + i['path'])

    def NewCreativeIcons(self):
        with open('datas/NewAssets.json', 'r') as Icons:
            Icons = json.load(Icons)
        for i in Icons:
            if i.startswith('FortniteGame/Content/Athena/Items/Consumables/PlaysetGrenade/'):
                path = i
                print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.BLUE + "Generating: " + Fore.GREEN + path)
                image = requests.get(f'https://fortnitecentral.gmatrixgames.ga/api/v1/export?path={path}')
                pathname = (path.split('FortniteGame/Content/Athena/Items/Consumables/PlaysetGrenade/')[-1])
                open(f'images/{pathname}.png', 'wb+').write(image.content)   
            

    def main(self):
        print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Generating data..")
        newcosmetics = requests.get('https://fortnite-api.com/v2/cosmetics/br/new').json()
        aes = requests.get('https://fortnitecentral.gmatrixgames.ga/api/v1/aes').json()
        #newassets = requests.get('https://benbot.app/api/v1/files/added').json()
        with open('datas/NewCosmetics.json', 'w') as file:
            json.dump(newcosmetics, file, indent=2)
        with open('datas/PakChunks.json', 'w') as file:
            json.dump(aes, file, indent=2)    
        #with open('datas/NewAssets.json', 'w') as file:
        #    json.dump(newassets, file, indent=2)  
        start = time.time()
        print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Info) " + Fore.WHITE + "Data Generated - Initializing..")
        self.LocChunksLoader()
        self.NewBackpacksIcons()
        self.NewCreativeIcons()
        self.NewEmotesIcons()
        self.NewPickaxeIcons()
        self.NewMusicsIcons()
        self.NewCosmeticsIcons()
        end = time.time()
        print(Fore.YELLOW + f"[{time.strftime('%H:%M')}] " + Fore.MAGENTA + "(Finished) " + Fore.WHITE + f"Data Generated in {round(end - start, 2)}")


if __name__ == "__main__":
    try:
        Main().main()
    except KeyboardInterrupt:
        exit(5)
