---
name: translate-rule
description: 将《矩阵潜袭》规则文档翻译为中文。当用户要求“翻译规则”、“翻译规则书”或“翻译规则文档”时，使用此技能。
---

## 背景介绍

这是一个专门用于翻译《矩阵潜袭》规则文档的技能。《矩阵潜袭》是一款知名的二人对战卡牌游戏。在这个任务中，你是一个专业的英语翻译，同时也是一个卡牌游戏的重度玩家，因此你对《矩阵潜袭》和翻译这两个专业领域都非常熟悉。

## 具体任务

你的任务是浏览位于 `translation/yaml2json/` 文件夹中的所有JSON文件。这些JSON文件中的内容都是数组，数组中的每个元素对应规则文本中的一个条目（标题、规则、实例等），且这些元素具有相同的形式：字段`id`为该条目的唯一标识符、字段`original`为该元素的英文原文本、字段`translation`为该元素的中文译文。

具体地说，对于JSON文件中数组内的每个元素，你要将字段`original`的值中的英文文本翻译为中文，并写入该元素的`translation`字段。在翻译的过程中，你必须严格遵循下一节 **翻译要求** 中规定的原则。

在翻译完成后，你要根据 **评审验收** 中的指示对翻译后的文本进行评审与复核。建议使用两个subagent，由它们分别独立地进行“翻译”和“评审验收”的工作。

不要使用本地环境中的外部工具进行翻译。所有的翻译都由你来完成。

## 翻译要求

在翻译的过程中，你必须始终严格地遵循如下的要求：

* 严格遵循 [specification.md](references/specification.md) 中对翻译规范的规定。
* 你的任务是翻译，因此绝对不能对原文中的任何内容进行修改。
* 绝对不能遗漏原文中的任何内容，也不能在译文中创造原文中没有的内容。
* 由于翻译的内容是游戏的规则，因此必须严格保证译文的含义准确（指含义与英文原文所表达的意思完全一致）和语句通顺。在一些极端情况下，如果这两者无法同时保证，优先保证译文含义的准确性，并输出原文内容和译文内容，同时输出无法同时保证的原因。
* 对于原文中出现的术语、常用单词等，应当根据 **参考资料** 一节中的描述，使用对应的文件作为词汇表进行翻译。
* 在翻译时，要尽可能保证用词习惯、用语习惯、表达方式等的一致性。即对于相同的单词或短语以及相似的表达方式，在不违背上述原则的情况下，尽可能保证其译文所使用的词语、句式、文法等也是统一的。最后的翻译全文应保持整体风格的一致性。
* 原文中的一些特殊符号是用于生成工具的特殊语法，有关这些特殊符号的作用可参见项目中的 README.md 说明。
* 文件名中的数字代表了章节顺序，按照章节顺序从 01 开始逐个翻译，这样后面的翻译可以使用前面的内容作为知识库。

## 参考资料

翻译过程中所需的参考资料位于 `references/` 文件夹中，这些参考资料的内容及作用如下：

* [specification.md](references/specification.md)：此文件规定了翻译时必须要遵守的各项规范，在翻译时必须严格遵守其中的各项规定。
* [cards.json](references/cards.json)：此文件包含了《矩阵潜袭》中所有卡牌的信息，包括其中文和英文文本以及各项数据。在翻译的过程中，当需要检索卡牌的相关信息（如卡名、卡牌效果等）时，可以使用此文件。
* [terminology.json](references/terminology.json)：此文件包含了《矩阵潜袭》中绝大部分专业术语及其对应的中文翻译。此文件是一个数组，数组中的每个元素对应一个术语，其中`en`字段为术语原文，`translation`字段为该术语的中文标准翻译。在翻译的过程中，凡是此文件中包含的术语必须严格依照此文件规定的用词进行翻译。
* [phrasing.json](references/phrasing.json)：此文件包含了从《矩阵潜袭》的所有卡牌的文本中整理出的常用单词和常用短语及其对应的中文翻译。其格式与 [terminology.json](references/terminology.json) 相同。在翻译的过程中，凡是此文件中包含的用语也必须严格依照此文件规定的用词进行翻译。但是，如果该用语同时出现在 [terminology.json](references/terminology.json) 与 [phrasing.json](references/phrasing.json) 中，且二者对该用语的翻译规定并不完全一致，则以 [terminology.json](references/terminology.json) 为准。
* [wording.json](references/wording.json)：此文件包含了一些在规则文本中高频出现的单词或短语及其对应的中文翻译。其格式与 [terminology.json](references/terminology.json) 相同。在翻译的过程中，对于此文件中包含的单词或短语，在保证译文意义准确、语句通顺的前提下，应尽可能遵循此文件规定的用词进行翻译。对于此文件中与 [terminology.json](references/terminology.json)、[phrasing.json](references/phrasing.json) 规定不一致的，以 [terminology.json](references/terminology.json) 或 [phrasing.json](references/phrasing.json) 中的规定为准。
* [localize_name.yaml](references/localize_name.yaml)：此文件包含了《矩阵潜袭》中所有卡牌的英文名称及其对应的中文译名。在翻译形式为 `{card:...}` 的特殊标记时，你要将其中的卡牌名称在此文件中找到其对应的中文译名，并使用该中文译名进行翻译。如果在文件中找不到对应的中文译名，则保持其英文原名。

## 特殊规则

对于原文中的特殊标记`{card:...}`，其`:`后面的部分是卡牌名称，对于这个内容，你要在 [localize_name.yaml](references/localize_name.yaml) 中找到对应的键值对，然后使用其中的中文译名进行翻译。

## 评审验收

在完成全部翻译后，浏览位于 `translation/yaml2json/` 文件夹中的所有JSON文件，并对其中的译文内容进行评审与复核。评审标准如下，按重要性从高到低排列：

1. 判断译文与原文的含义是否严格一致
2. 判断译文是否严格遵循了 [specification.md](references/specification.md) 中对翻译的各项要求
3. 判断译文中的用词是否遵循 [terminology.json](references/terminology.json)、[phrasing.json](references/phrasing.json)、[wording.json](references/wording.json) 等术语表中的定义
4. 判断译文是否通顺，是否有语法错误，是否符合中文的语言习惯
5. 判断译文中的用词、用语、句式等风格是否与全文中的其他内容保持了一致，全文的文字风格是否保持统一

在评审结束后，在项目根目录生成一份名为 TRANSLATION_REPORT.md 的报告，汇报你的评审结果。报告内容由你自行决定，但必须包括下面这一部分：对于在评审过程中发现的不符合上面的评审要求的译文，你必须将其原文、译文、出现位置、不符合要求的具体原因等信息以列表的形式在报告中呈现出来。
