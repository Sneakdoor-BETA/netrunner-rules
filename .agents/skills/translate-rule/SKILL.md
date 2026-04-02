---
name: translate-rule
description: 将《矩阵潜袭》规则文档翻译为中文。当用户要求“翻译规则”、“翻译规则书”或“翻译规则文档”时，使用此技能。
---

## 背景介绍

这是一个专门用于翻译《矩阵潜袭》规则文档的技能。《矩阵潜袭》是一款知名的二人对战卡牌游戏。在这个任务中，你是一个专业的英语翻译，同时也是一个卡牌游戏的重度玩家，因此你对《矩阵潜袭》和翻译这两个专业领域都非常熟悉。

## 具体任务

你的任务分为两部分：**翻译文档** 与 **评审验收**。这两部分工作的具体内容如下：

### 翻译文档

在这一步，你的任务是浏览位于 `translation/input/` 文件夹中的所有YAML文件。这些YAML文件以结构化的形式编写了《矩阵潜袭》的规则文本，其组织结构与一些特殊标记语法参见 [README.md](references/README.md)。

对于每个YAML文件，创建一个subagent，由这个subagent执行翻译任务。具体地说，每个subagent的任务如下：在YAML文件中，所有键为 `text`、`snippet` 和 `toc_entry` 的值都是需要翻译的文本内容。subagent需要将这些内容翻译为中文，其他内容保持不变，完成后仍以YAML格式保存至 `translation/output`，文件名与原YAML文件相同（如果 `translation/output` 已存在该文件，将其覆盖）。在翻译的过程中，你必须严格遵循 **翻译规范** 中规定的原则。

在所有的翻译任务都完成之后，根据 **评审验收** 一节中的指示对翻译后的文本进行评审与复核。

#### 翻译规范

在翻译的过程中，你必须始终严格地遵循如下的要求：

* 根据 [README.md](references/README.md) 理解原文的组织结构及特殊标记语法。
* 严格遵循 [specification.md](references/specification.md) 中对翻译规范的规定。
* 你的任务是翻译，因此绝对不能对原文中的任何内容进行修改。
* 绝对不能遗漏原文中的任何内容，也不能在译文中创造原文中没有的内容。
* 由于翻译的内容是游戏的规则，因此必须严格保证译文的含义准确（指含义与英文原文所表达的意思完全一致）和语句通顺。在一些极端情况下，如果这两者无法同时保证，优先保证译文含义的准确性，并输出原文内容和译文内容，同时输出无法同时保证的原因。
* 对于原文中出现的术语、常用单词等，应当根据 **参考资料** 一节中的描述，使用对应的文件作为词汇表进行翻译。
* 在翻译时，要尽可能保证用词习惯、用语习惯、表达方式等的一致性。即对于相同的单词或短语以及相似的表达方式，在不违背上述原则的情况下，尽可能保证其译文所使用的词语、句式、文法等也是统一的。最后的翻译全文应保持整体风格的一致性。
* 原文中的一些特殊符号是用于生成工具的特殊语法，有关这些特殊符号的作用可参见项目中的 README.md 说明。

#### 注意事项

在翻译的过程中，注意如下事项：

* 不要使用本地环境中的外部工具进行翻译。所有的翻译都由你来完成。
* 如果 `translation/output/` 中有已存在的翻译后的文档，忽略之，在翻译过程中不要参考这些内容。
* 除了 `translation/input/` 中待翻译的文档原文和 [reference/](references/) 文件夹中的参考资料，项目中的其他文件与本次翻译任务无关，无需查看这些无关文件。

### 评审验收

在这一步，你的任务是在完成全部翻译后，浏览位于 `translation/output/` 文件夹中的所有YAML文件，并对其中的译文内容进行评审与验收。这些YAML文件的组织结构和格式、及其中特殊标记的语法可参见 [README.md](references/README.md)。

`translation/output/` 的文件与 `translation/input/` 中的文件应当是一一对应的，前者是后者的译文。对于 `translation/output/` 中的每个YAML文件，创建一个subagent，由这个subagent执行评审验收任务。具体地说，该subagent的任务是评判该YAML文件中的译文是否符合如下的标准（按重要性从高到低排列）：

1. 检查YAML文件格式是否正确
2. 判断译文与原文的含义是否严格一致
3. 判断译文是否严格遵循了 [specification.md](references/specification.md) 中对翻译的各项要求
4. 判断译文中的用词是否遵循 [terminology.json](references/terminology.json)、[phrasing.json](references/phrasing.json)、[wording.json](references/wording.json) 等术语表中的定义
5. 判断译文是否通顺，是否有语法错误，是否符合中文的语言习惯
6. 判断译文中的用词、用语、句式等风格是否与全文中的其他内容保持了一致，全文的文字风格是否保持统一

评审验收工作只需要对译文的质量进行评定，不需要对译文中出现的问题进行修改。在所有的评审都结束后，你需要将所有subagent的评审结果进行汇总整理，在项目根目录生成一份名为 TRANSLATION_REPORT.md 的报告。报告内容由你自行决定，但必须包括下面这一部分：对于在评审过程中发现的不符合上面的评审要求的译文，你必须将其原文、译文、出现位置、不符合要求的具体原因等信息以列表的形式在报告中呈现出来。

## 参考资料

翻译过程中所需的参考资料位于 `references/` 文件夹中，这些参考资料的内容及作用如下：

* [README.md](references/README.md)：此文件描述了 `translation/input` 中待翻译的YAML文件的组织结构和格式，以及特殊标记语法的参考。
* [specification.md](references/specification.md)：此文件规定了翻译时必须要遵守的各项规范，在翻译时必须严格遵守其中的各项规定。
* [terminology.json](references/terminology.json)：此文件包含了《矩阵潜袭》中绝大部分专业术语及其对应的中文翻译。此文件是一个数组，数组中的每个元素对应一个术语，其中`en`字段为术语原文，`translation`字段为该术语的中文标准翻译。在翻译的过程中，凡是此文件中包含的术语必须严格依照此文件规定的用词进行翻译。
* [phrasing.json](references/phrasing.json)：此文件包含了从《矩阵潜袭》的所有卡牌的文本中整理出的常用单词和常用短语及其对应的中文翻译。其格式与 [terminology.json](references/terminology.json) 相同。在翻译的过程中，凡是此文件中包含的用语也必须严格依照此文件规定的用词进行翻译。但是，如果该用语同时出现在 [terminology.json](references/terminology.json) 与 [phrasing.json](references/phrasing.json) 中，且二者对该用语的翻译规定并不完全一致，则以 [terminology.json](references/terminology.json) 为准。
* [wording.json](references/wording.json)：此文件包含了一些在规则文本中高频出现的单词或短语及其对应的中文翻译。其格式与 [terminology.json](references/terminology.json) 相同。在翻译的过程中，对于此文件中包含的单词或短语，在保证译文意义准确、语句通顺的前提下，应尽可能遵循此文件规定的用词进行翻译。对于此文件中与 [terminology.json](references/terminology.json)、[phrasing.json](references/phrasing.json) 规定不一致的，以 [terminology.json](references/terminology.json) 或 [phrasing.json](references/phrasing.json) 中的规定为准，其优先级为：terminology.json > phrasing.json > wording.json。
* [localize_name.yaml](references/localize_name.yaml)：此文件包含了《矩阵潜袭》中所有卡牌的英文名称及其对应的中文译名。在翻译形式为 `{card:...}` 的特殊标记时，你要将其中的卡牌名称在此文件中找到其对应的中文译名，并使用该中文译名进行翻译。如果在文件中找不到对应的中文译名，则保持其英文原名。
