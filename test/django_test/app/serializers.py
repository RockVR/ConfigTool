# This file is auto-generated, please don't modify it directly.
# Modify source xls file and use model_gen to regenerate again.
#
# Last generate time: 2018-05-23 13:11:16

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
			'GoldPerTime',
			'AddGoldNum',
			'MaxGoldNum',
			'LogicGameParam',
		]

class ActorMobileSerializer(serializers.ModelSerializer):

	class Meta:
		model = ActorMobile
		fields = [
			'id',
			'ActorName',
			'Coin',
			'Mint',
			'Exp',
			'Level',
			'BeginDay',
			'GameLogicDrierAddExp',
			'GameLogicLaserAddExp',
			'GameLogicDrierAddHappy',
			'GameLogicLaserAddHappy',
			'DailyTaskGetTime',
			'BuyMedicineNum',
			'ActorID',
		]

class GiftMobileSerializer(serializers.ModelSerializer):

	class Meta:
		model = GiftMobile
		fields = [
			'id',
			'CoinNum',
			'CardStaticID',
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

class TaskEventMobileSerializer(serializers.ModelSerializer):

	class Meta:
		model = TaskEventMobile
		fields = [
			'id',
			'EventType',
			'EventParam',
		]

class TaskOwnMobileSerializer(serializers.ModelSerializer):

	class Meta:
		model = TaskOwnMobile
		fields = [
			'id',
			'TaskType',
			'TaskID',
			'TaskFinish',
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

class CatSoundStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = CatSoundStatic
		fields = [
			'id',
			'CatID',
			'AnimationName',
			'SoundNameArray',
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
			'ProductID',
			'ShopItemNum',
			'ShopItemSequence',
			'ShopItemCNPrice',
			'ShopItemENPrice',
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

class CatOwnMobileSerializer(serializers.ModelSerializer):

	class Meta:
		model = CatOwnMobile
		fields = [
			'id',
			'OwnItemType',
			'OwnItemID',
			'EuipOrNot',
			'OwnNum',
			'CatID',
		]

class CatMobileSerializer(serializers.ModelSerializer):

	class Meta:
		model = CatMobile
		fields = [
			'id',
			'CatStaticID',
			'CatName',
			'CatAge',
			'LevelPoint',
			'HappyPoint',
			'HungryPoint',
			'HealthPoint',
			'ExpPoint',
			'WeightPoint',
			'CatBirthday',
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
			'TimeMin',
			'TimeMax',
			'GoldMin',
			'GoldMax',
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

class CardBagStaticSerializer(serializers.ModelSerializer):

	class Meta:
		model = CardBagStatic
		fields = [
			'id',
			'CardBagType',
			'CardBagProbability',
		]

class CardStaticSerializer(serializers.ModelSerializer):
	CardBagID = CardBagStaticSerializer(read_only=True)

	class Meta:
		model = CardStatic
		fields = [
			'id',
			'CardBagID',
			'CardProbability',
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
			'BgSoundName_ARRoom',
			'BgSoundName_3DRoom',
			'BgSoundName_FittingRoom',
			'CommonSound_GetCoin',
			'CommonSound_GetCard',
			'CommonSound_OpenView',
			'CommonSound_GetSunperCard',
		]

class CostumeStaticSerializer(serializers.ModelSerializer):
	CostumeName = LanguageStaticSerializer(read_only=True)
	CostumeMatchedCat = CatStaticSerializer(read_only=True)

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
			'CostumeMatchedCat',
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

class CatPathStaticSerializer(serializers.ModelSerializer):
	TriggerGrassID = PropStaticSerializer(read_only=True)
	TriggerBaseCardBagID = CardBagStaticSerializer(read_only=True)
	TriggerRareCardBagID = CardBagStaticSerializer(read_only=True)
	TriggerToyCardBagID1 = CardBagStaticSerializer(read_only=True)
	TriggerToyCardBagID2 = CardBagStaticSerializer(read_only=True)
	TriggerToyCardBagID3 = CardBagStaticSerializer(read_only=True)
	TriggerToyCardBagID4 = CardBagStaticSerializer(read_only=True)
	TriggerToyCardBagID5 = CardBagStaticSerializer(read_only=True)
	TriggerToyCardBagID6 = CardBagStaticSerializer(read_only=True)

	class Meta:
		model = CatPathStatic
		fields = [
			'id',
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
			'TriggerToyCardConditionID5',
			'TriggerCardProbability5',
			'TriggerToyCardBagID5',
			'TriggerToyCardConditionID6',
			'TriggerCardProbability6',
			'TriggerToyCardBagID6',
		]

