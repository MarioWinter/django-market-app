from rest_framework import serializers
from market_app.models import Market, Seller

def validate_no_x(value):
    errors = []
    
    if "Iran" in value:
        errors.append("no Iran in location")
    if "Tunesien" in value:
        errors.append("no Tunesien in location")
    if errors:
        raise serializers.ValidationError(errors)
    return value


class MarketSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255, validators=[validate_no_x])
    description = serializers.CharField()
    net_worth = serializers.DecimalField(max_digits=100, decimal_places=2)
    
    def create(self, validated_data):
        return Market.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.description = validated_data.get('description', instance.description)
        instance.net_worth = validated_data.get('net_worth', instance.net_worth)
        instance.save()
        return instance


class SellerDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        name = serializers.CharField(max_length=255)
        contact_info = serializers.CharField()
        markets = MarketSerializer(many=True, read_only=True) #Nested Serializer aber keine Vererbung eher eine Verschachtelung aller Merkte des Sellers
        #markets = serializers.StringRelatedField(many=True)


class SellerCreateSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)
        contact_info = serializers.CharField()
        markets = serializers.ListField(child=serializers.IntegerField(), write_only=True)
        
        def validate_markets(self, value):#Ids aus der markets listField in der classe mit dem neuen Seller drin
            markets = Market.objects.filter(id__in=value)#markets aus dem Market object der Datenbank
            if len(markets) != len(value):#vergelicht die anzahl der märkte
                raise serializers.ValidationError("Markets anzahl: "  + str(markets) + " Anzahl Value: "+ str(value))#Debugging
            return value
        
        def create(self, validated_data):
            market_ids = validated_data.pop('markets')#holt sich die ids aus den validierten daten nach is_vailded() in der view
            seller = Seller.objects.create(**validated_data)#Beinhaltet die Validierten Daten des Sellers
            markets = Market.objects.filter(id__in=market_ids)#filtert aus der Market Datenbank nur die Märkte raus deren Ids Valide und aus der eingabe sind. 
            seller.markets.set(markets)#fügt im Seller das Spalte Markets die gefilterten Markets ein.
            return seller#gibt den Seller zurück