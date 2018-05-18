# This file is auto-generated, please don't modify it directly.
# Modify source xls file and use model_gen to regenerate again.
#
# Last generate time: 2018-05-18 13:51:01

from rest_framework import serializers
from .models import *

class GameStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = GameStatic
		fields = [
			'id',
			'GameType',
			'GameIcon',
			'GameResource',
			'GameDescription',
			'MinHungryNum',
			'HappyPerTime',
			'AddHappyNum',
			'MaxHappyNum',
			'ExpPerTime',
			'AddExpNum',
			'MaxExpNum',
			'LogicGameParam',
		]

class FoodStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = FoodStatic
		fields = [
			'id',
			'FoodType',
			'UnlockCatAge',
			'UnlockCoin',
			'UnlockEnjoy',
			'Coin',
			'Mint',
			'HungryPoint',
			'HappyPoint',
			'LevelPoint',
			'HealthPoint',
			'FoodIconName',
		]

class CatStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = CatStatic
		fields = [
			'id',
			'CatType',
			'CatBaseResource',
			'CatWholeBodyMeshName',
			'CatBodyNotEarMeshName',
			'CatPartResource',
			'IdleBehaviorParam',
			'FeedBehaviorParam',
			'LazerBehaviorParam',
			'DryerBehaviorParam',
			'HealthPoint',
			'HealthMaxPoint',
			'WeightPoint',
			'WeightMaxPoint',
			'ExpPoint',
			'ExpAddTimeSpan',
			'ExpAddNum',
			'HappyPointAddHealthPoint',
			'HungryPointAddHealthPoint',
			'HappyInitialPoint',
			'HappyMaxPoint',
			'HungryInitialPoint',
			'HungryMaxPoint',
			'LevelPoint',
			'MaxLevelPoint',
			'NexLevelID',
		]

class ExpAddStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = ExpAddStatic
		fields = [
			'id',
			'LevelPoint',
			'ExpPoint',
		]

class WeightAddStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = WeightAddStatic
		fields = [
			'id',
			'WeightNumHealthZeroPoint',
			'WeightNumHealthOnePoint',
			'WeightNumHealthTwoPoint',
			'WeightNumHealthThreePoint',
			'WeightNumHealthFourPoint',
			'WeightNumHealthFivePoint',
		]

class AudioStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = AudioStatic
		fields = [
			'id',
			'Describe',
			'AudioType',
			'AudioName',
			'AudioVolumn',
			'AudioLoopParamName',
			'Audio3DMinDistance',
			'Audio3DMaxDistance',
		]

class GoldMintShopStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = GoldMintShopStatic
		fields = [
			'id',
			'ShopItemType',
			'ShopItemTagType',
			'ShopItemPrice',
			'ShopItemNum',
			'ShopItemSequence',
		]

class PropShopStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = PropShopStatic
		fields = [
			'id',
			'ShopItemType',
			'ShopItemID',
			'ShopItemPrice',
			'ShopItemNum',
			'ShopItemSequence',
		]

class UserGuideConditionStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserGuideConditionStatic
		fields = [
			'id',
			'UserGuideConditionType',
			'ConditionParam',
		]

class UserGuideEventStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserGuideEventStatic
		fields = [
			'id',
			'UserGuideEventType',
			'EventParam',
			'NextGuideEventIDArray',
		]

class CatLevelStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = CatLevelStatic
		fields = [
			'id',
			'LevelNum',
			'ExpNum',
		]

class LanguageStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = LanguageStatic
		fields = [
			'id',
			'LanguageEngInfo',
			'LanguageChnInfo',
		]

class DialogStaticSerializer(serializers.ModelSerializer):
	DialogTitle = LanguageStaticSerializer(read_only=True)
	DialogInfo = LanguageStaticSerializer(read_only=True)

	class Meta:
		model = DialogStatic
		fields = [
			'id',
			'DialogType',
			'DialogTitle',
			'DialogInfo',
		]

class PropStaticSerializer(serializers.ModelSerializer):
	PropName = LanguageStaticSerializer(read_only=True)
	PropDescirption = LanguageStaticSerializer(read_only=True)

	class Meta:
		model = PropStatic
		fields = [
			'id',
			'PropType',
			'PropName',
			'PropDescirption',
			'PropIcon',
			'PropMaxNum',
			'Coin',
			'Mint',
		]

class DailyTaskStaticSerializer(serializers.ModelSerializer):
	DailyTaskName = LanguageStaticSerializer(read_only=True)

	class Meta:
		model = DailyTaskStatic
		fields = [
			'id',
			'DailyTaskName',
			'DailyTaskProbability',
			'EventType',
			'TaskEventNum',
		]

class DailyTaskRewardStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = DailyTaskRewardStatic
		fields = [
			'id',
			'DayNum',
			'CreditExp',
			'CreditCoin',
			'CreditMint',
			'CreditPropID',
			'CreditCostum',
		]

class SevenDaySignStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = SevenDaySignStatic
		fields = [
			'id',
			'DayNum',
			'AddCoin',
			'AddPropID',
		]

class CatPathStaticSerializer(serializers.ModelSerializer):
	PathName = LanguageStaticSerializer(read_only=True)
	PathDescirption = LanguageStaticSerializer(read_only=True)

	class Meta:
		model = CatPathStatic
		fields = [
			'id',
			'PathName',
			'PathDescirption',
			'TriggerGrassID',
			'TriggerHealthPointMin',
			'TriggerHealthPointMax',
			'TriggerCatLevelMin',
			'TriggerCatLevelMax',
			'TriggerBaseCardBagID',
			'TriggerRareCardBagID',
			'TriggerToyCardConditionID1',
			'TriggerCardProbability1',
			'TriggerToyCardBagID1',
			'TriggerToyCardConditionID2',
			'TriggerCardProbability2',
			'TriggerToyCardBagID2',
			'TriggerToyCardConditionID3',
			'TriggerCardProbability3',
			'TriggerToyCardBagID3',
			'TriggerToyCardConditionID4',
			'TriggerCardProbability4',
			'TriggerToyCardBagID4',
		]

class CardBagStaticSerializer(serializers.ModelSerializer):
	CardBagDescirption = LanguageStaticSerializer(read_only=True)

	class Meta:
		model = CardBagStatic
		fields = [
			'id',
			'CardBagType',
			'CardBagProbability',
			'CardBagDescirption',
		]

class CardStaticSerializer(serializers.ModelSerializer):
	CardBagID = CardBagStaticSerializer(read_only=True)
	CardName = LanguageStaticSerializer(read_only=True)
	CardDescirption = LanguageStaticSerializer(read_only=True)

	class Meta:
		model = CardStatic
		fields = [
			'id',
			'CardBagID',
			'CardProbability',
			'CardName',
			'CardDescirption',
			'CardRes',
			'CardStar',
			'RecycleCoin',
		]

class ConstStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = ConstStatic
		fields = [
			'id',
			'CatTriggerTime',
			'MaxRestoreCardNum',
		]

class CostumeStaticSerializer(serializers.ModelSerializer):
	CostumeName = LanguageStaticSerializer(read_only=True)

	class Meta:
		model = CostumeStatic
		fields = [
			'id',
			'CostumeType',
			'BodyWithEar',
			'CostumeResource',
			'CostumeHangPoint',
			'CostumeName',
			'CostumeCharm',
			'CostumePrice',
			'MintPrice',
			'CostumeIconName',
		]

class AnimationStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = AnimationStatic
		fields = [
			'id',
			'AnimationName',
			'AnimationStateName',
			'AnimationParamName',
			'AnimationParamVariable',
			'AnimationParam2Name',
			'AnimationParam2Variable',
		]

class UserGuideStaticSerializer(serializers.ModelSerializer):
	UserGuideCondition = UserGuideConditionStaticSerializer(read_only=True)
	UserGuideEvent = UserGuideEventStaticSerializer(read_only=True)

	class Meta:
		model = UserGuideStatic
		fields = [
			'id',
			'UserGuideCondition',
			'UserGuideEvent',
			'NextGuideID',
		]

